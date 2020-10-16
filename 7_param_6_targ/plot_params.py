import numpy as np
import matplotlib.pyplot as plt


dat1 = np.loadtxt('limit_cycles_combined.txt',delimiter=',',skiprows=1)




for param in range(1,7):
	fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))
	i = 1
	for ax_row in axes:
		for ax in ax_row:
			ax.scatter(dat1[:8496,param],dat1[:8496,i],s=0.1)
			ax.scatter(dat1[8496:,param],dat1[8496:,i],s=0.1)
			i += 1
	plt.show()

