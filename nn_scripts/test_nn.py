import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, random_split
from myDataloader import LSGENDataset 
from RMSE import RMSELoss
from myNN import Net

# Load the training data
ID_file = 'limit_cycles_combined.txt'
#ID_file = 'GLCL_1/limit_cycles_1_normalised.txt'
LSGEN_dataset = LSGENDataset(ID_file)

train_size = int(0.8 * len(LSGEN_dataset))
test_size = len(LSGEN_dataset) - train_size
print(train_size, test_size)
train_dataset, test_dataset = random_split(LSGEN_dataset, [train_size, test_size])

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True, num_workers=8)
test_dataloader = DataLoader(test_dataset, batch_size=8, shuffle=True, num_workers=8)

enum = enumerate(test_dataloader,0)
print(enum)

net = Net()
print("NN details:")
print(net)
print("\n\n")


## NN training
import torch.optim as optim

lr = 0.001
optimizer = optim.Adam(net.parameters(), lr=lr)
criterion = RMSELoss()
'''
for i in range(3):
	optimizer.zero_grad()
	inp = torch.randn(1,1,360)
	out = net(inp)
	print(out)
	target = torch.randn(1,1,3)
	print(target)
	loss = criterion(out, target)
	print(loss)
	loss.backward()
	optimizer.step()
'''
net = net.double()

targs = []
preds = []
for j,data in enumerate(test_dataloader,0):
	inputs, targets = data['dat'],data['vals']
	outputs = net(inputs)
	targs.append(targets)
	preds.append(outputs)
	if j == 400:
		break

np.save('mymodels/preds_prior.npy',[targs, preds])
