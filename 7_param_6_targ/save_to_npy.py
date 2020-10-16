import numpy as np

ID_dat = np.loadtxt('limit_cycles_combined.txt',skiprows=1,delimiter=',')

n_cycles = ID_dat.shape[0]




x = np.empty(shape=(n_cycles, 200, 900))

for i in range(n_cycles):
	if i%np.round(n_cycles/20) == 0:
		print("{} %".format(np.round(100*i/n_cycles)))

	ID, p, batch = int(ID_dat[i,0]), int(ID_dat[i,-2]), int(ID_dat[i,-1])
	x[i,:,:] = np.load('GLCL_{}/LCL_p{}_{}_s0_m270_f3_c10_area/cycle_{}_area_norm.npy'.format(batch,p,batch,ID))

x = x.reshape(n_cycles*200, 900)

np.savez_compressed('X_area.npz', x)
'''

y_small = ID_dat[:,1:-2]
print(y_small.shape)
y = np.empty(shape=(n_cycles, 200, 6))
for i in range(n_cycles):
	for j in range(200):
		y[i,j,:] = y_small[i,:]

y = y.reshape(n_cycles*200, 6)

np.savez_compressed('y.npz', y)
'''
