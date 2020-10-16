import torch
from myNN import Net
import numpy as np

DATA = 'data_vectors_3'
n_snaps = 8
n_test = 20
p = np.zeros(shape=(n_test,6))

for n in range(n_test):
	dat = np.zeros(shape=(n_snaps,135))

	for i in range(n*n_snaps,(n+1)*n_snaps):
		real = np.load(DATA+'/img{}.npy'.format(i))
		dat[i%8,:] = 0.003*real[:270:2]

	dat = dat.reshape(1,-1)
	dat = torch.from_numpy(dat)


	model = Net()
	model.double()
	model.load_state_dict(torch.load('mymodels/mymodel_7'))

	l = model(dat).tolist()[0]
	for param in range(6):
		p[n,param] = l[param]

print(p)
print()
m = np.mean(p,axis=0)
st = np.std(p,axis=0)
print(m)
print(st)
print()
K = 1.5*m[0]
ea = m[1]
Mk = 0.02 + 0.06*m[2]
va = m[3]
St = 0.74 + 12.92*m[4]
beta = 2+8*m[5]
print('K:\t{}'.format(K))
print('ea:\t{}'.format(ea))
print('Mk:\t{}'.format(Mk))
print('va:\t{}'.format(va))
print('St:\t{}'.format(St))
print('beta:\t{}'.format(beta))
