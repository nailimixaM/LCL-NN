import numpy as np
import matplotlib.pyplot as plt


f = 'preds_prior.npy'

t,p = np.load('preds_prior.npy',allow_pickle=True)
print(t.shape,p.shape)
print(t[:10])

for i in range(t.shape[0]):
	bt = t[i]
	bp = p[i]
	for j in range(bt.shape[0]):
		rt = bt[j]
		rp = bp[j]		
		print(rt,rp)
		print(type(rt))
		_ = input()
		#plt.scatter(rp[0].detach.numpy(),rt[0]).detach.numpy()

plt.show()
