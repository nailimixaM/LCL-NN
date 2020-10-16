import numpy as np
import matplotlib.pyplot as plt
import sys

dat = np.load('nn_3/output_3/preds_{}.npy'.format(sys.argv[1]),allow_pickle=True)
print(dat.shape)

t = dat[0]
p = dat[1]

print(t.shape)
print(t[0].shape)
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

'''
m_errors = (mt-mp)**2
sorted_inds = np.argsort(m_errors)
print(m_errors[sorted_inds[:-5]])
plt.scatter(Et[sorted_inds[:-10]],Ft[sorted_inds[:-10]])
plt.show()
_ = input()
'''

kR = np.sqrt(np.sum((kt-kp)**2)/n)
eR = np.sqrt(np.sum((Et-Ep)**2)/n)
mR = np.sqrt(np.sum((mt-mp)**2)/n)
vR = np.sqrt(np.sum((Vt-Vp)**2)/n)
fR = np.sqrt(np.sum((Ft-Fp)**2)/n)
bR = np.sqrt(np.sum((Bt-Bp)**2)/n)
print(kR)
print(eR)
print(mR)
print(vR)
print(fR)
print(bR)

'''					
plt.scatter(et,ep,s=5)
plt.plot([0,1.3],[0,1.3],c='r')
plt.show()
'''
K_max,ea_max,Mk_max,va_max,f_max,beta_max =1.0,1.0,1.0,1.0,1.0,1.0
fig, ((ax_k,ax_e,ax_m),(ax_v,ax_f,ax_b)) = plt.subplots(nrows=2, ncols=3, figsize=(16, 12))

ax_k.set_title('K')
ax_k.scatter(kt*K_max,kp*K_max,s=.05)
ax_k.plot([0.,1.],[0.,1.],c='r')

ax_e.set_title('ea')
ax_e.scatter(Et*ea_max,Ep*ea_max,s=.05)
ax_e.plot([0.,1.],[0.,1.],c='r')

ax_m.set_title('Mk')
ax_m.scatter(mt*Mk_max,mp*Mk_max,s=.05)
ax_m.plot([0.,1.],[0.,1.],c='r')

ax_v.set_title('va')
ax_v.scatter(Vt*va_max,Vp*va_max,s=.05)
ax_v.plot([0.,1.],[0.,1.],c='r')

ax_f.set_title('St')
ax_f.scatter(Ft*f_max,Fp*f_max,s=.05)
ax_f.plot([0.,1.],[0.,1.],c='r')

ax_b.set_title('beta')
ax_b.scatter(Bt*beta_max,Bp*beta_max,s=.05)
ax_b.plot([0.,1.],[0.,1.],c='r')
plt.show()
