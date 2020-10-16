import numpy as np
import matplotlib.pyplot as plt

fname = 'GLCL_5/LCL_p3000_5_s0_m270_f2_c8/cycle_5601_snaps_norm.npy'

d = np.load(fname)
plt.plot(d[99])
plt.show()
