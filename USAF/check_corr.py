import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

f = 'limit_cycles_combined.txt'

#d = np.loadtxt(f,delimiter=',',skiprows=1)
d = pd.read_csv(f,sep=",",header=0,usecols=['K','ea','Mk','va','St','beta'])

corr = d.corr()
print(corr)

plt.figure()
#plt.heatmap(corr,xticklabels=corr.columns,yticklabels=corr.columns)
plt.imshow(corr,cmap='hot')
plt.colorbar()
plt.show()
