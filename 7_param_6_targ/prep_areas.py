import numpy as np
import os
import sys

batch = int(sys.argv[1])
skip_initial = 0 #skip elements at beginning of data vector
max_i = 270
shrink_factor = 3
n_snap = 10 #number snapshots to combine into single input vector
sf = 2500 #real sampling frequency
p_min = 3000
p_max = 9000
p_vfr = 3000
dat_length = int(np.ceil((max_i-skip_initial)/shrink_factor))
print(dat_length)

### Area calculator
def calc_area(dx, y):

        n_area = y.shape[0] - 1
        a = np.empty(n_area)

        for i in range(n_area):
                r1, r2 = y[i], y[i+1]
                a[i] = np.pi*(r1+r2)*np.sqrt(dx**2 + (r1-r2)**2)

        return a

#############################################################
#Load and calc area
IDs,Ls,ps = np.loadtxt('GLCL_{}/limit_cycles_{}.txt'.format(batch,batch),usecols=(0,7,-1),unpack=True,skiprows=1,delimiter=',')

for i,cycle in enumerate(IDs):
	cycle = int(cycle)
	p = int(ps[i])
	L = Ls[i]
	vfr = int(p/200)

	SRC_DIR = 'GLCL_{}/LCL_p{}_{}/'.format(batch,p,batch)
	DST_DIR = 'GLCL_{}/LCL_p{}_{}_s{}_m{}_f{}_area/'.format(batch,p,batch,skip_initial,max_i,shrink_factor)

	if not os.path.isdir(DST_DIR):
		os.mkdir(DST_DIR)

	SAVE_DIR = DST_DIR+'cycle_{}/'.format(cycle)
	print(SAVE_DIR)
	if not os.path.isdir(SAVE_DIR):
		os.mkdir(SAVE_DIR)

	for step in range(vfr,p+1,vfr):
		fname = SRC_DIR+'cycle_{}/xover_{}.npy'.format(cycle,step)
		dat = np.load(fname)
		dat = calc_area(1/20, dat/L)
		new_dat = dat[skip_initial:max_i:shrink_factor]
		assert new_dat.shape[0] == dat_length
		np.save(SAVE_DIR+'area_{}.npy'.format(step),new_dat)

#############################################################
#Combine each cycle into a matrix where each row is a set of steps
IDs,Fs,ps = np.loadtxt('GLCL_{}/limit_cycles_{}.txt'.format(batch,batch),usecols=(0,5,-1),unpack=True,skiprows=1,delimiter=',')
for i,cycle in enumerate(IDs):
	
	ID = int(cycle)	
	p = int(ps[i])
	vfr = int(p/200)
	
	SRC_DIR = 'GLCL_{}/LCL_p{}_{}_s{}_m{}_f{}_area/'.format(batch,p,batch,skip_initial,max_i,shrink_factor)
	DST_DIR = 'GLCL_{}/LCL_p{}_{}_s{}_m{}_f{}_c{}_area/'.format(batch,p,batch,skip_initial,max_i,shrink_factor,n_snap)
	
	if not os.path.isdir(DST_DIR):
		os.mkdir(DST_DIR)

	f = int(Fs[i])
	ratio = round((p*f/sf)/vfr)
	print('Combining {}-{}-{}-{}'.format(p,ID,f,ratio))
	src = SRC_DIR + 'cycle_{}/'.format(ID)
	comb_dat = np.zeros(shape=(200,dat_length))
	for step in range(vfr,p+1,vfr):
		step_dat = np.load(src+'area_{}.npy'.format(step)).reshape(1,-1)
		comb_dat[int(step/vfr - 1)] = step_dat

	#np.save(DST_DIR+'cycle_{}_dat.npy'.format(ID),comb_dat)
	comb_snap_dat = np.zeros(shape=(200,dat_length*n_snap))
	snaps = np.zeros(shape=(n_snap,dat_length))

	for start in range(200):
		for snap in range(n_snap):
			ix = int(start + snap*ratio)%200
			snap_dat = comb_dat[ix]
			snaps[snap] = snap_dat

		comb_snap_dat[start] = snaps.reshape(1,-1)

	np.save(DST_DIR+'cycle_{}_area.npy'.format(ID),comb_snap_dat)
