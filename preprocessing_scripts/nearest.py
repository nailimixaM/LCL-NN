import numpy as np


IDs,Ks,eas,Mks,vas,fs,betas,ps,bs = np.loadtxt('limit_cycles_combined.txt',skiprows=1,unpack=True,delimiter=',')

Ks = Ks + 1
eas = eas/2 + 1/2
Mks = Mks/20 + 1/20
vas = vas/2 + 1/2
fs = fs*230 + 270
betas = betas*4 + 5

batch = 1
p = 3000
cycle = 1
step = 15
tf = 'GLCL_{}/LCL_p{}_{}_s0_m270_f2/cycle_{}/xover_{}.npy'.format(batch,p,batch,cycle,step)
tdat = np.load(tf)/0.003

max_diff = 0.04*1.5

for i,cycle in enumerate(IDs):
	cycle = int(cycle)
	p = int(ps[i])
	batch = int(bs[i])
	vfr = int(p/200)
	
	for step in range(vfr,p+1,vfr):
		f = 'GLCL_{}/LCL_p{}_{}_s0_m270_f2/cycle_{}/xover_{}.npy'.format(batch,p,batch,cycle,step)

		dat = np.load(f)/0.003

		diff = np.sum((tdat-dat)**2)
		if diff < max_diff:
			print('{}-{}-{}-{}'.format(batch,p,cycle,step))
			print(diff)
			print("{},{},{},{},{},{}".format(Ks[i],eas[i],Mks[i],vas[i],fs[i],betas[i]))
		#_ = input()
	
