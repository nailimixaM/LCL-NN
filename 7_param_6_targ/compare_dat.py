import numpy as np
import matplotlib.pyplot as plt

dat = np.loadtxt('limit_cycles_combined.txt',skiprows=1,delimiter=',', usecols=(0,-1,-2))

print(dat.shape)

c, b, p = dat[0,:]
c = int(c)
p = int(p)
b = int(b)
f1 = 'GLCL_{}/LCL_p{}_{}_s{}_m{}_f{}_c{}/cycle_{}_snaps_norm.npy'.format(b,p,b,0,270,2,8,c)

dat1 = np.load(f1)
plt.plot(dat1[0,:])

c, b, p = dat[-2,:]
c = int(c)
p = int(p)
b = int(b)
f1 = 'GLCL_{}/LCL_p{}_{}_s{}_m{}_f{}_c{}/cycle_{}_snaps_norm.npy'.format(b,p,b,0,270,2,8,c)

print(np.load(f1))
dat1 = np.load(f1)
plt.plot(dat1[0,:])

plt.show()
