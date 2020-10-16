import numpy as np
import matplotlib.pyplot as plt


f = 'GLCL_1/LCL_p3000_1_s0_m270_f2/cycle_1/xover_15.npy'

dat = np.load(f)

plt.scatter(np.arange(len(dat)),dat)

batch = 1
p = 3000
cycle = 229
step = 390
f = 'GLCL_{}/LCL_p{}_{}_s0_m270_f2/cycle_{}/xover_{}.npy'.format(batch,p,batch,cycle,step)

dat = np.load(f)

plt.scatter(np.arange(len(dat)),dat)
plt.show()
