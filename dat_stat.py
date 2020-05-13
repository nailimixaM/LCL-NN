import numpy as np

IDs,ps = np.loadtxt('GLCL_1/limit_cycles_1.txt',skiprows=1,unpack=True,usecols=(0,9),dtype='int',delimiter=',')
print(IDs.shape)

n_cycles = IDs.shape[0]

tot = np.zeros(shape=(n_cycles*200,100))

ii = 0
for i,cycle in enumerate(IDs):
	p = ps[i]
	vfr = int(p/200)
	print(p,cycle)

	for step in range(vfr,p+1,vfr):
		d = np.load('GLCL_1/LCL_p{}_1_mi200_sf2/cycle_{}/xover_{}.npy'.format(p,cycle,step))
		tot[ii,:] = d.reshape(1,-1)
		ii += 1
		#print(tot[:5,:10])
		#_ = input()

	
	if i == n_cycles-1:
		break

print(np.mean(tot,axis=0), np.std(tot,axis=0))
print(np.mean(tot,axis=0).shape, np.std(tot,axis=0).shape)

np.save('inputs_mean.npy',np.mean(tot,axis=0))
np.save('inputs_std.npy',np.std(tot,axis=0))

