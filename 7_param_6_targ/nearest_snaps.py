import numpy as np
import matplotlib.pyplot as plt


IDs,Ks,eas,Mks,vas,fs,betas,Ls,Us,ps,bs = np.loadtxt('limit_cycles_combined.txt',skiprows=1,unpack=True,delimiter=',')
'''
Ks = Ks + 1
eas = eas/2 + 1/2
Mks = Mks/20 + 1/20
vas = vas/2 + 1/2
fs = fs*230 + 270
betas = betas*4 + 5
'''

batch = 1
p = 3000
cycle = 5
row = 1
tf = 'GLCL_{}/LCL_p{}_{}_s0_m270_f2_c8/cycle_{}_snaps.npy'.format(batch,p,batch,cycle)
tdat = np.load(tf)[0,:]/0.003
#print(tdat[:10])
#_ = input()

max_diff = 0.5*2

for i,cycle in enumerate(IDs):
	#if i == 2:
#		continue

	cycle = int(cycle)
	p = int(ps[i])
	batch = int(bs[i])
	
	f = 'GLCL_{}/LCL_p{}_{}_s0_m270_f2_c8/cycle_{}_snaps.npy'.format(batch,p,batch,cycle)
	mat_dat = np.load(f)/0.003

	for row in range(200):
		dat = mat_dat[row,:]
		#print(dat[:10])
		#_ = input()
		diff = np.sum((tdat-dat)**2)
		if diff < max_diff:
			print('{}-{}-{}-{}'.format(batch,p,cycle,row))
			print(diff)
			print("{},{},{},{},{},{},{},{}".format(Ks[i],eas[i],Mks[i],vas[i],fs[i],betas[i],Ls[i],Us[i]))
			#plt.scatter(np.arange(len(dat)),tdat)
			#plt.scatter(np.arange(len(dat)),dat)
			#plt.show()
			break
		#_ = input()
	
