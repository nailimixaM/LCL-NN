import numpy as np
import torch
from myNN import Net

model = Net()

model.load_state_dict(torch.load('mymodels/mymodel_400'))
print(model)

''' Test first line of limit_cycles_combined.txt'''
test1 = np.load('GLCL_1/LCL_p3000_1_s0_m71_f1_c6/cycle_3_snaps_norm.npy')[0]
test1 = test1.reshape(1,426)
test1 = torch.from_numpy(test1).float() 
out1 = model(test1)
#print(out1)

''' Test USAF data '''
for start in range(2210, 2280):
	usaf = np.zeros(shape=(6,71))
	for i in range(6):
		ID = start + i
		usaf1 = np.load('12_knots/vec/img{}.npy'.format(ID))[:71].flatten()
		usaf[i,:] = usaf1


	usaf = usaf.reshape(1,426)
	usaf = torch.from_numpy(usaf).float() 
	out = model(usaf)
	print(out)

