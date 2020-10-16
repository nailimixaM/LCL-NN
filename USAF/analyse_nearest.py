import numpy as np
import matplotlib.pyplot as plt

with open('nearest.log') as f:
	lines = f.readlines()

n = 500
dat = np.zeros(shape=(n,6))
for i in range(n):
	#print(lines[i])
	d = lines[2+3*i].strip('\n').split(',')
	for j in range(6):
		print(d[j])
		dat[i,j] = float(d[j])

print(dat[0,:])

#print(dat[:,4]*dat[:,5])
#for i in range(1,6):
#	plt.scatter(dat[:,0],dat[:,i])
#	plt.show()
plt.scatter(dat[:,0],dat[:,4]*dat[:,5])
plt.show()
