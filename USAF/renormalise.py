import numpy as np


for batch in range(1,6):
	dat = np.loadtxt('GLCL_{}/limit_cycles_{}.txt'.format(batch,batch),skiprows=1,delimiter=',')

	for i, cycle in enumerate(dat[:,0]):
		p = int(dat[i,-1])
		cycle = int(cycle)
		radius = dat[i,7]
		#print(radius)

		fname = 'GLCL_{}/LCL_p{}_{}_s0_m71_f1_c6/cycle_{}_snaps.npy'.format(batch,p,batch,cycle)
		fdat = np.load(fname)/radius
		#print(fdat)
		oname = 'GLCL_{}/LCL_p{}_{}_s0_m71_f1_c6/cycle_{}_snaps_norm.npy'.format(batch,p,batch,cycle)
		np.save(oname,fdat)
		
		#input()
		
print(batch," done")

