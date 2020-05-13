import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt


class LSGENDataset(Dataset):
	def __init__(self, ID_file):
		self.ID_data = np.loadtxt(ID_file,skiprows=1,delimiter=',')
	
	def __len__(self):
		#print(self.ID_data.shape[0])	
		return self.ID_data.shape[0]*200

	def idx_to_identity(self,idx):
                cycle_num = idx//200
                #row = idx%200
                p = int(self.ID_data[cycle_num,-2])
                batch = int(self.ID_data[cycle_num,-1])
                step = int((p/200)*(1+idx-200*cycle_num))
                cycle = int(self.ID_data[cycle_num, 0])
                return batch, p, cycle, step

	def __getitem__(self,idx):
                if torch.is_tensor(idx):
                        idx = idx.tolist()

                cycle_num = idx//200

                #Params to estimate
                vals = self.ID_data[cycle_num, 1:-2] #ignore ID, p, batch
                vals = np.array([vals])
                vals = vals.astype('double').reshape(1, -1)

                #Inputs (flame shape)
                batch, p, cycle, step = self.idx_to_identity(idx)
                fname = 'GLCL_{}/LCL_p{}_{}_mi{}_sf{}_n{}/cycle_{}/xover_{}.npy'.format(batch,p,batch,200,2,8,cycle,step)
                dat = np.load(fname).reshape(1,-1)

                #Return shape-params pair
                sample = {'dat': dat, 'vals': vals}
                return sample




#Test class
#ID_file = 'GLCL_1/limit_cycles_1.txt'
ID_file = 'limit_cycles_combined.txt'
Ldatset = LSGENDataset(ID_file)
print(len(Ldatset))
print(Ldatset.__getitem__(199)['dat'].shape)
print(Ldatset.__getitem__(199)['dat'][:10])
print(Ldatset.__getitem__(199)['vals'])
print(Ldatset.__getitem__(200)['vals'])
print(Ldatset.__getitem__(len(Ldatset)-1)['vals'])



'''
print(Ldatset.__getitem__(199)['dat'])
print(Ldatset.__getitem__(199)['dat'].shape)
print(Ldatset.__getitem__(199)['vals'])
plt.plot(Ldatset.__getitem__(200)['dat'][0])
plt.show()
'''

