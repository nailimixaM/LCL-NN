import numpy as np
import matplotlib.pyplot as plt

fname = 'GLCL_1/LCL_p3000_1_4snap/cycle_5_snaps.npy'

d = np.load(fname)
plt.plot(d[99])
plt.show()
