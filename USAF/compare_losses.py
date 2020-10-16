import numpy as np
import sys
import matplotlib.pyplot as plt


d = np.load('mymodels/losses_{}.npy'.format(sys.argv[1]))
d2 = np.load('mymodels_8_frames/losses_{}.npy'.format(sys.argv[1]))
d3 = np.load('mymodels_10_frames/losses_{}.npy'.format(sys.argv[1]))

test_set = 0

n = d.shape[1]
plt.scatter(1+np.arange(n),d[test_set,:],s=5,label='6 frames')
plt.scatter(1+np.arange(n),d2[test_set,:],s=5,label='8 frames')
plt.scatter(1+np.arange(n),d3[test_set,:],s=5,label='10 frames')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()

plt.scatter(1+np.arange(n),d[test_set,:],s=5,label='6 frames')
plt.scatter(1+np.arange(n),d2[test_set,:],s=5, label='8 frames')
plt.scatter(1+np.arange(n),d3[test_set,:],s=5, label='10 frames')
plt.show()

