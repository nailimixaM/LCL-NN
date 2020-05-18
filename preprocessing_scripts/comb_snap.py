import numpy as np
import sys
import os

batch = int(sys.argv[1])
n_snap = 8
sf = 2500


for p in range(3000,9001,3000):
	IDs,Fs = np.loadtxt('limit_cycles_p{}_{}.txt'.format(p,batch),delimiter=',',usecols=(0,5),unpack=True)
	vfr = int(p/200)
	dst_dir = 'LCL_p{}_{}_{}snap/'.format(p,batch,n_snap)
	if not os.path.isdir(dst_dir):
		os.mkdir(dst_dir)


	for i in range(IDs.shape[0]):
                ID = int(IDs[i])
                f = Fs[i]
                print('{}-{}-{}'.format(p,ID,f))
                ratio = round((p*f/sf)/vfr)
                print(ratio)

                src='LCL_p{}_{}_shorco/cycle_{}_dat.npy'.format(p,batch,ID)

                comb_dat = np.load(src)
                comb_snap_dat = np.zeros(shape=(200,117*n_snap))
                snaps = np.zeros(shape=(n_snap,117))

                for start in range(200):
                        for snap in range(n_snap):
                                ix = int(start + snap*ratio)%200
                                snap_dat = comb_dat[ix]
                                snaps[snap] = snap_dat

                        comb_snap_dat[start] = snaps.reshape(1,-1)


                np.save(dst_dir+'cycle_{}_snaps.npy'.format(ID),comb_snap_dat)
