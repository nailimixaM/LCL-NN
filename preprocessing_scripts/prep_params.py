import numpy as np
import sys

batch = int(sys.argv[1])

output_file = 'GLCL_{}/limit_cycles_{}.txt'.format(batch,batch)

dat = np.loadtxt(output_file,delimiter=',',skiprows=1)
for col in range(1,9):
        print(max(dat[:,col]))

fo = open('GLCL_{}/limit_cycles_{}_normalised.txt'.format(batch,batch),'w')

K_max,ea_max,Mk_max,va_max,f_max,beta_max,L_max,U_max =2.0,1.0,0.1,1.0,500.0,9.0,0.003,1.0
K_min,ea_min,Mk_min,va_min,f_min,beta_min,L_min,U_min =0.0,0.0,0.0,0.0,40.0,1.0,0.003,1.0

fo.write('ID,K,ea,Mk,va,f,beta,p\n')
for i in range(len(dat)):
	ID,K,ea,Mk,va,f,beta,L,U,p = dat[i]

	K = (K - 1)*2/K_max
	ea = (ea - 0.5)*2/ea_max
	Mk = (Mk - 0.05)*2/Mk_max
	va = (va - 0.5)*2/va_max
	f = (f - 270)*2/(f_max - f_min)
	beta = (beta - 5)*2/(beta_max - beta_min)

	fo.write('{},{},{},{},{},{},{},{}\n'.format(int(ID),K,ea,Mk,va,f,beta,p))

fo.close()
