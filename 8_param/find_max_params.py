import numpy as np

batch = 1
f = 'GLCL_{}/limit_cycles_{}_normalised.txt'.format(batch,batch)

dat = np.loadtxt(f,delimiter=',',skiprows=1)

for i in range(1,9):
	print(min(dat[:,i]))
