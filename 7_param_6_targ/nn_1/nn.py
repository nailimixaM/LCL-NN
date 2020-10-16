import numpy as np
import time
import torch
from torch.utils.data import Dataset, DataLoader, random_split
from myDataloader import LSGENDataset 
from RMSE import RMSELoss
from myNN import Net
import resource
import os
import sys
import psutil

#rlimit = resource.getrlimit(resource.RLIMIT_NOFILE)
#resource.setrlimit(resource.RLIMIT_NOFILE, (2048*3, rlimit[1]))


def main():
	process = psutil.Process(os.getpid())
	### INPUTS ###
	ID_file = 'limit_cycles_combined.txt'
	#ID_file = 'GLCL_5/limit_cycles_5_to_6.txt'
	dat_split = 0.8
	n_workers = 8
	train_batch_size = 2000
	test_batch_size = 2000
	n_test = 10
	lr = 0.001
	n_epochs = 400
	dst = sys.argv[1]
	if not os.path.isdir(dst):
		os.mkdir(dst)

	# Load the training data
	LSGEN_dataset = LSGENDataset(ID_file)

	train_size = int(dat_split * len(LSGEN_dataset))
	test_size = len(LSGEN_dataset) - train_size
	print("Train size: {}\nTest size: {}".format(train_size, test_size))
	train_dataset, test_dataset = random_split(LSGEN_dataset, [train_size, test_size])

	train_dataloader = DataLoader(train_dataset, batch_size=train_batch_size, shuffle=True, num_workers=n_workers, multiprocessing_context="forkserver")
	test_dataloader = DataLoader(test_dataset, batch_size=test_batch_size, num_workers=n_workers, multiprocessing_context="forkserver")

	net = Net()
	print("\n")
	print("NN details:")
	print(net)
	print("\n")


	## NN training
	import torch.optim as optim
	optimizer = optim.Adam(net.parameters(), lr=lr)
	criterion = RMSELoss()
	train_loss_tracker = []
	test_loss_tracker = []
	net = net.double()


	#print("Memory before training loop:", process.memory_info().rss)
	print("Beginning training...")
	for epoch in range(n_epochs):
		#print("Memory before training loop, epoch{}:".format(epoch), process.memory_info().rss)
		train_loss = 0
		test_loss = 0
		for i, data in enumerate(train_dataloader, 0):
			inputs, targets = data['dat'],data['vals']
			optimizer.zero_grad()
			outputs = net(inputs)
			loss = criterion(outputs, targets)
			loss.backward()
			optimizer.step()
			train_loss += loss.item()

		train_loss /= i+1
		train_loss_tracker.append(train_loss)

		#At end of epoch, evaluate on test data
		#print("Memory before testing loop, epoch{}:".format(epoch), process.memory_info().rss)
		targs = []
		preds = []
		for j,data in enumerate(test_dataloader,0):
			inputs, targets = data['dat'],data['vals']
			outputs = net(inputs)
			loss = criterion(outputs, targets)
			test_loss += loss.item()
			targs.append(targets)
			preds.append(outputs)
			if j == n_test-1:
				break

		test_loss /= j+1
		test_loss_tracker.append(test_loss)
		print('[epoch {}] train loss: {},\ttest loss: {}'.format(epoch+1, train_loss, test_loss))

		np.save('{}/preds_{}.npy'.format(dst, epoch+1),[targs, preds])
		torch.save(net.state_dict(), '{}/mymodel_{}'.format(dst, epoch+1))    
		np.save('{}/losses_{}.npy'.format(dst, epoch+1),[train_loss_tracker, test_loss_tracker])

	print("Finished training")


if __name__ == "__main__":
	main()
