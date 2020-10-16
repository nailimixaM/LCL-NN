import numpy as np
import matplotlib.pyplot as plt
import sys

d = np.loadtxt('limit_cycles_combined.txt',skiprows=1,delimiter=',')
d = d[:,1:9]

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 12))

i = 0
for row in axes:
	for ax in row:
		ax.scatter(d[:,0],d[:,i],s=5)
		i += 1

'''

ax_k.set_title('K')
ax_k.scatter(kt*K_max,kp*K_max,s=5)
ax_k.plot([0.,1.],[0.,1.],c='r')

ax_e.set_title('ea')
ax_e.scatter(Et*ea_max,Ep*ea_max,s=5)
ax_e.plot([0.,1.],[0.,1.],c='r')

ax_m.set_title('Mk')
ax_m.scatter(mt*Mk_max,mp*Mk_max,s=5)
ax_m.plot([0.,1.],[0.,1.],c='r')

ax_v.set_title('va')
ax_v.scatter(Vt*va_max,Vp*va_max,s=5)
ax_v.plot([0.,1.],[0.,1.],c='r')

ax_f.set_title('f')
ax_f.scatter(Ft*f_max,Fp*f_max,s=5)
ax_f.plot([0.,1.],[0.,1.],c='r')

ax_b.set_title('beta')
ax_b.scatter(Bt*beta_max,Bp*beta_max,s=5)
ax_b.plot([0.,1.],[0.,1.],c='r')

ax_l.set_title('L')
ax_l.scatter(lt*l_max,lp*l_max,s=5)
ax_l.plot([0.,1.],[0.,1.],c='r')

ax_u.set_title('U')
ax_u.scatter(ut*u_max,up*u_max,s=5)
ax_u.plot([0.,1.],[0.,1.],c='r')
'''
plt.show()

