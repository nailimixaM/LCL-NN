import numpy as np
import matplotlib.pyplot as plt


f = 'GLCL_1/LCL_p3000_1_mi200_sf2_n8/cycle_1/xover_15.npy'

dat = np.load(f)

plt.scatter(np.arange(800),dat)

batch = 4
p = 6000
cycle = 5665
step = 870
f = 'GLCL_{}/LCL_p{}_{}_mi200_sf2_n8/cycle_{}/xover_{}.npy'.format(batch,p,batch,cycle,step)

dat = np.load(f)

plt.scatter(np.arange(800),dat)
plt.show()
