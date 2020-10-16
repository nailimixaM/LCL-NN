import torch
from myNN import Net
import numpy as np
import sys
import matplotlib.pyplot as plt


out_file = 'my_nn_data_4.txt'
of = open(out_file, 'w')

for case in range(1,11):
	DATA = f'y_area_{case}.npz'

	tot_dat = np.load(DATA)['arr_0']
	print(tot_dat.shape)

	model = Net()
	model.double()
	model.load_state_dict(torch.load('mymodels/mymodel_400'))

	new_dat = torch.from_numpy(tot_dat)
	p = model(new_dat).tolist()

	print(p)
	print()
	m = np.mean(p,axis=0)
	st = np.std(p,axis=0)
	print(m)
	print(st)
	print()
	K = 2.5*m[0]
	ea = m[1]
	Mk = 0.02 + 0.06*m[2]
	va = m[3]
	St = 2*np.pi*(0.74 + 12.92*m[4])
	beta = 2+8*m[5]
	print('K:\t{}'.format(K))
	print('ea:\t{}'.format(ea))
	print('Mk:\t{}'.format(Mk))
	print('va:\t{}'.format(va))
	print('St:\t{}'.format(St))
	print('beta:\t{}'.format(beta))

	print(K, ea, Mk, va, St, beta)
	of.write(f'{K} {ea} {Mk} {va} {St} {beta}\n')
