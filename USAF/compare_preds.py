import numpy as np
import matplotlib.pyplot as plt
import sys

models = ['mymodels', 'mymodels_8_frames', 'mymodels_10_frames']
n_models = len(models)

max_step = int(sys.argv[1])
increment = 1
if len(sys.argv)>2:
	increment = int(sys.argv[2])

n = max_step//increment
KRMSE = np.zeros(shape=(n_models,n))
ERMSE = np.zeros(shape=(n_models,n))
MRMSE = np.zeros(shape=(n_models,n))
VRMSE = np.zeros(shape=(n_models,n))
FRMSE = np.zeros(shape=(n_models,n))
BRMSE = np.zeros(shape=(n_models,n))

for model_i in range(n_models):
	model = models[model_i]
	z = 0

	for step in range(1,max_step+1,increment):
		dat = np.load(model+'/preds_{}.npy'.format(step),allow_pickle=True)

		t = dat[0]
		p = dat[1]

		Kt = []
		Kp = []
		et = []
		ep = []
		Mt = []
		Mp = []
		vt = []
		vp = []
		ft = []
		fp = []
		bt = []
		bp = []
		for i in range(10):
			for j in range(2000):
				tij = t[i][j].detach().numpy()
				Kij,eij,Mij,vij,fij,bij=tij[0]
				Kt.append(Kij)
				et.append(eij)
				Mt.append(Mij)
				vt.append(vij)
				ft.append(fij)
				bt.append(bij)
				pij = p[i][j].detach().numpy()
				Kij,eij,Mij,vij,fij,bij=pij[0]
				Kp.append(Kij)
				ep.append(eij)
				Mp.append(Mij)
				vp.append(vij)
				fp.append(fij)
				bp.append(bij)

		#RMSE calcs
		n = len(Kt)
		kt = np.array(Kt)
		kp = np.array(Kp)
		Et = np.array(et)
		Ep = np.array(ep)
		mt = np.array(Mt)
		mp = np.array(Mp)
		Vt = np.array(vt)
		Vp = np.array(vp)
		Ft = np.array(ft)
		Fp = np.array(fp)
		Bt = np.array(bt)
		Bp = np.array(bp)

		kR = np.sqrt(np.sum((kt-kp)**2)/n)
		eR = np.sqrt(np.sum((Et-Ep)**2)/n)
		mR = np.sqrt(np.sum((mt-mp)**2)/n)
		vR = np.sqrt(np.sum((Vt-Vp)**2)/n)
		fR = np.sqrt(np.sum((Ft-Fp)**2)/n)
		bR = np.sqrt(np.sum((Bt-Bp)**2)/n)
		#print(kR)
		#print(eR)
		#print(mR)
		#print(vR)
		#print(fR)
		#print(bR)
		KRMSE[model_i, z] = kR
		ERMSE[model_i, z] = eR
		MRMSE[model_i, z] = mR
		VRMSE[model_i, z] = vR
		FRMSE[model_i, z] = fR
		BRMSE[model_i, z] = bR
		z += 1

'''					
plt.scatter(et,ep,s=5)
plt.plot([0,1.3],[0,1.3],c='r')
plt.show()
'''
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(16,12))
i = 0
for ax_row in ax:
	for ax_i in ax_row:	
		if i == 0:
			dat = KRMSE
			title = 'K'
		elif i == 1:
			dat = ERMSE
			title = 'ea'
		elif i == 2:
			dat = MRMSE
			title = 'Mk'
		elif i == 3:
			dat = VRMSE
			title = 'va'
		elif i == 4:
			dat = FRMSE
			title = 'St'
		elif i == 5:
			dat = BRMSE
			title = 'beta'

		for j in range(n_models):
			ax_i.scatter(np.arange(1,max_step+1,increment), dat[j,:], label=models[j])

		ax_i.set_ylim(0,0.25)
		ax_i.set_title(title)
		ax_i.legend()
		i += 1

plt.show()
