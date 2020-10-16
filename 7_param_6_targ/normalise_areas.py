import numpy as np

tot = np.zeros(200)

#Find average of first area element
n = 0
for batch in range(1,6):
	dat = np.loadtxt('GLCL_{}/limit_cycles_{}.txt'.format(batch,batch),skiprows=1,delimiter=',')

	for i, cycle in enumerate(dat[:,0]):
		p = int(dat[i,-1])
		cycle = int(cycle)

		fname = 'GLCL_{}/LCL_p{}_{}_s0_m270_f3_c10_area/cycle_{}_area.npy'.format(batch,p,batch,cycle)
		#fname = 'GLCL_{}/LCL_p{}_{}_s0_m270_f3_c10_area/cycle_{}_area_norm.npy'.format(batch,p,batch,cycle)
		tot += np.load(fname)[:,0]
		n += 1
		
	print(batch, n," done")

avg = np.sum(tot/200/n)
print(avg)

'''
#Normalise areas
for batch in range(1,6):
	dat = np.loadtxt('GLCL_{}/limit_cycles_{}.txt'.format(batch,batch),skiprows=1,delimiter=',')

	for i, cycle in enumerate(dat[:,0]):
		p = int(dat[i,-1])
		cycle = int(cycle)

		fname = 'GLCL_{}/LCL_p{}_{}_s0_m270_f3_c10_area/cycle_{}_area.npy'.format(batch,p,batch,cycle)
		fdat = np.load(fname)/avg

		oname = 'GLCL_{}/LCL_p{}_{}_s0_m270_f3_c10_area/cycle_{}_area_norm.npy'.format(batch,p,batch,cycle)
		np.save(oname,fdat)
		
		
	print(batch," done")
'''
