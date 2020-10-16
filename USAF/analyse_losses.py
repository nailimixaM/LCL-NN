import numpy as np
import sys
import matplotlib.pyplot as plt


d = np.load('mymodels/losses_{}.npy'.format(sys.argv[1]))
print(d.shape)

n = d.shape[1]
plt.scatter(1+np.arange(n),d[0,:],s=1)
plt.scatter(1+np.arange(n),d[1,:],s=1)
plt.yscale('log')
plt.xscale('log')
plt.show()

plt.scatter(1+np.arange(n),d[0,:],s=1)
plt.scatter(1+np.arange(n),d[1,:],s=1)
plt.show()

