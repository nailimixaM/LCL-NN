import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

ID_dat = np.loadtxt('limit_cycles_combined.txt',usecols=0,dtype='int',skiprows=1,delimiter=',')

print(ID_dat.shape)

n_cyc = 4

dat = np.zeros(shape=(n_cyc*200,135))

for i, cyc in enumerate(ID_dat):
	if i == n_cyc:
		break
	for step in range(15,3015,15):
		fn = 'GLCL_1/LCL_p3000_1_s0_m270_f2/cycle_{}/xover_{}.npy'.format(cyc,step)
		fd = np.load(fn)
		dat[i,:] = fd.reshape(1,-1)


'''
X = np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
X_emb = TSNE().fit_transform(X)
'''
X = dat
X_emb = TSNE().fit_transform(X)


print(X_emb.shape)
colors = ['r','b','g','y']
for i in range(n_cyc*200):
	plt.scatter(X_emb[i,0],X_emb[i,1],c=colors[i//200])
plt.show()
