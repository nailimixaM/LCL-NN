import numpy as np
import sys

batch = int(sys.argv[1])

output_file = 'GLCL_{}/limit_cycles_{}.txt'.format(batch,batch)

dat = np.loadtxt(output_file,delimiter=',',skiprows=1)

fo = open('GLCL_{}/limit_cycles_{}_to_6.txt'.format(batch,batch),'w')

def normed(p,pmax,pmin): #norm to range 0 to 1
	if pmax == pmin:
		return p

	p =  (p - (pmax+pmin)/2)/(pmax-pmin) + 0.5
	return p

K_max,ea_max,Mk_max,va_max,f_max,beta_max,L_max,U_max =2.5,1.0,0.08,1.0,500.0,10.0,0.004,5.0
K_min,ea_min,Mk_min,va_min,f_min,beta_min,L_min,U_min =0.0,0.0,0.02,0.0,200.0,2.0,0.002,1.0
fo.write('ID,K,ea,Mk,va,St,beta,p,batch\n')

St_max = f_max*beta_max*L_max/U_min
St_min = f_min*beta_min*L_min/U_max
print(St_min,St_max)
St_max = 13.66 
St_min = 0.74
print(St_min,St_max)

for i in range(len(dat)):
	ID,K,ea,Mk,va,f,beta,L,U,p = dat[i]

	St = f*L*beta/U

	K = normed(K,K_max,K_min)
	ea = normed(ea,ea_max,ea_min)
	Mk = normed(Mk,Mk_max,Mk_min)
	va = normed(va,va_max,va_min)
	beta = normed(beta,beta_max,beta_min)
	St = normed(St,St_max,St_min)

	fo.write('{},{},{},{},{},{},{},{},{}\n'.format(int(ID),K,ea,Mk,va,St,beta,p,batch))

fo.close()
