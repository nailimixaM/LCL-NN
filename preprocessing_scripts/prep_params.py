import numpy as np
import sys

nparam = int(sys.argv[1])
batch = int(sys.argv[2])

output_file = 'GLCL_{}/limit_cycles_{}.txt'.format(batch,batch)

dat = np.loadtxt(output_file,delimiter=',',skiprows=1)

fo = open('GLCL_{}/limit_cycles_{}_normalised.txt'.format(batch,batch),'w')

'''
def normed(p,pmax,pmin): #norm to range -1 to 1
	return 2*(p - (pmax+pmin)/2)/(pmax-pmin)
'''

def normed(p,pmax,pmin): #norm to range 0 to 1
	if pmax == pmin:
		return p

	p =  (p - (pmax+pmin)/2)/(pmax-pmin) + 0.5
	return p

if nparam == 6:
	K_max,ea_max,Mk_max,va_max,f_max,beta_max,L_max,U_max =2.0,1.0,0.1,1.0,500.0,9.0,0.003,1.0
	K_min,ea_min,Mk_min,va_min,f_min,beta_min,L_min,U_min =0.0,0.0,0.0,0.0,40.0,1.0,0.003,1.0
	fo.write('ID,K,ea,Mk,va,f,beta,p,batch\n')

elif nparam == 8:
	K_max,ea_max,Mk_max,va_max,f_max,beta_max,L_max,U_max =1.5,1.0,0.08,1.0,500.0,10.0,0.004,5.0
	K_min,ea_min,Mk_min,va_min,f_min,beta_min,L_min,U_min =0.0,0.0,0.02,0.0,200.0,2.0,0.002,1.0
	fo.write('ID,K,ea,Mk,va,f,beta,L,U,p,batch\n')


for i in range(len(dat)):
	ID,K,ea,Mk,va,f,beta,L,U,p = dat[i]

	K = normed(K,K_max,K_min)
	ea = normed(ea,ea_max,ea_min)
	Mk = normed(Mk,Mk_max,Mk_min)
	va = normed(va,va_max,va_min)
	f = normed(f,f_max,f_min)
	beta = normed(beta,beta_max,beta_min)
	L = normed(L,L_max,L_min)
	U = normed(U,U_max,U_min)

	'''
	K = (K - 1)*2/K_max
	ea = (ea - 0.5)*2/ea_max
	Mk = (Mk - 0.05)*2/Mk_max
	va = (va - 0.5)*2/va_max
	f = (f - 270)*2/(f_max - f_min)
	beta = (beta - 5)*2/(beta_max - beta_min)
	'''

	if nparam == 6:
		fo.write('{},{},{},{},{},{},{},{},{}\n'.format(int(ID),K,ea,Mk,va,f,beta,p,batch))
	elif nparam == 8:
		fo.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(int(ID),K,ea,Mk,va,f,beta,L,U,p,batch))

fo.close()
