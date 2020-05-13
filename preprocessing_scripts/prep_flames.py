import numpy as np
import os
import sys

#############################################################
# Script to preprocess flames into NN-digestable format
# requires:
# - cycles and ID files in folders GLCL_*
# - input: batch

batch = int(sys.argv[1])

max_i = 200
shrink_factor = 2
n_snap = 8 #number snapshots to combine into single input vector
sf = 2500 #real sampling frequency
dat_length = int(np.ceil(max_i/shrink_factor))

SRC = 'GLCL_{}/'.format(batch)

#############################################################
#Cut and shrink
IDs,ps = np.loadtxt(SRC+'limit_cycles_{}.txt'.format(batch),unpack=True,usecols=(0,9),dtype='int',skiprows=1,delimiter=',')
for i,cycle in enumerate(IDs):
	p = ps[i]
	vfr = int(p/200)

	SRC_DIR = 'GLCL_{}/LCL_p{}_{}/'.format(batch,p,batch)
	DST_DIR= 'GLCL_{}/LCL_p{}_{}_mi{}_sf{}/'.format(batch,p,batch,max_i,shrink_factor)

	if not os.path.isdir(DST_DIR):
		os.mkdir(DST_DIR)
	
	SAVE_DIR = DST_DIR+'cycle_{}/'.format(cycle)
	print(SAVE_DIR)
	if not os.path.isdir(SAVE_DIR):
		os.mkdir(SAVE_DIR)

	for step in range(vfr,p+1,vfr):
		fname = SRC_DIR+'cycle_{}/xover_{}.npy'.format(cycle,step)
		dat = np.load(fname)
		new_dat = dat[:max_i:shrink_factor]
		new_dat = 2*new_dat/0.003 - 1 #Normalise between -1 and 1 
		assert new_dat.shape[0] == dat_length

		np.save(SAVE_DIR+'xover_{}.npy'.format(step),new_dat)


#############################################################
#Combine n_snaps into into one vector for each timestep + normalisation
IDs,Fs,ps = np.loadtxt(SRC+'limit_cycles_{}.txt'.format(batch),unpack=True,usecols=(0,5,9),skiprows=1,delimiter=',')
mean = np.load('inputs_mean.npy')
std = np.load('inputs_std.npy')

for i,ID in enumerate(IDs):
	ID = int(ID)
	p = int(ps[i])
	f = Fs[i]
	vfr = int(p/200)

	SRC_DIR = 'GLCL_{}/LCL_p{}_{}_mi{}_sf{}/'.format(batch,p,batch,max_i,shrink_factor)
	DST_DIR = 'GLCL_{}/LCL_p{}_{}_mi{}_sf{}_n{}/'.format(batch,p,batch,max_i,shrink_factor,n_snap)
	
	if not os.path.isdir(DST_DIR):
		os.mkdir(DST_DIR)

	ratio = round((p*f/sf)/vfr)
	print('Combining {}-{}-{}-{}'.format(p,ID,f,ratio))
	src = SRC_DIR + 'cycle_{}/'.format(ID)
	dst = DST_DIR + 'cycle_{}/'.format(ID)
	if not os.path.isdir(dst):
		os.mkdir(dst)

	for start in range(200):
		snaps = np.zeros(shape=(n_snap,dat_length))
		for snap in range(n_snap):
			ix = int(start + snap*ratio)%200
			step = int((1+ix)*vfr)
			snap_dat = np.load(src+'xover_{}.npy'.format(step)).reshape(1,-1)
			#snaps[snap,:] = (snap_dat-mean)/std
			snaps[snap,:] = snap_dat

		snaps = snaps.reshape(1,-1)
		np.save(dst+'xover_{}.npy'.format(step),snaps)

