import numpy as np
import matplotlib.pyplot as plt
import sys


if len(sys.argv) > 1:
	fname = sys.argv[1]
	d = np.load(fname)[99]
else:
	fname = 'GLCL_5/LCL_p3000_5_s0_m270_f3_c10/cycle_5601_snaps_norm.npy'
	d = np.load(fname)

print(d[:10])
plt.plot(d)
plt.show()
