import numpy as np
import sys

batch = sys.argv[1]

#f = 'GLCL_{}/limit_cycles_{}_to_6.txt'.format(batch,batch)
f = 'limit_cycles_combined.txt'

dat = np.loadtxt(f,delimiter=',',skiprows=1)
for i in range(1,7):
	print(min(dat[:,i]))


for i in range(1,7):
	print(max(dat[:,i]))

'''
f = 'GLCL_{}/limit_cycles_{}.txt'.format(batch,batch)

dat = np.loadtxt(f,delimiter=',',skiprows=1)

for i in range(1,9):
	print(min(dat[:,i]))

print("#"*5)
print(max(dat[:,5]*dat[:,6]*dat[:,7]/dat[:,8]))
print(min(dat[:,5]*dat[:,6]*dat[:,7]/dat[:,8]))
print("#"*5)

for i in range(1,9):
	print(max(dat[:,i]))
'''

