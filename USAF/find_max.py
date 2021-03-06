import numpy as np

n_batch = 2

max_i = 0

for batch in range(1,n_batch+1):
	IDs,ps = np.loadtxt('SLCL_{}/limit_cycles_{}_normalised.txt'.format(batch,batch),skiprows=1,delimiter=',',unpack=True,usecols=(0,4))

	print(len(IDs))
	for i in range(len(IDs)):
		p = int(ps[i])
		cycle = int(IDs[i])
		vfr = int(p/200)
		for step in range(vfr,p+1,vfr):
			f = 'SLCL_{}/LCL_p{}_{}/cycle_{}/xover_{}.npy'.format(batch,p,batch,cycle,step)
			dat = np.load(f)
			for j in range(359,max_i,-1):
				if dat[j] > 0:
					max_i = j
					print(batch,p,cycle,step,max_i)
					break
					
