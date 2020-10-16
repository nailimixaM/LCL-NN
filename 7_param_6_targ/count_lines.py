import numpy as np

run_tot = 0
for b in range(1,6):
	print("##### {} #####".format(b))
	#with open('GLCL_{}/limit_cycles_{}_to_6.txt'.format(b,b),'r') as f:
	with open('GLCL_{}/limit_cycles_{}.txt'.format(b,b),'r') as f:
		lines = f.readlines()
		n_lines = len(lines)

		if lines[0][:2] == 'ID':
			print(b,lines[0])
			n_lines -= 1

	print(b,n_lines)
	
	tot = 0
	for p in range(3000,12000,3000):
		with open('GLCL_{}/limit_cycles_p{}_{}.txt'.format(b,p,b),'r') as f:
			lines = f.readlines()
			n_lines = len(lines)

			if lines[0][:2] == 'ID':
				print(b,p,lines[0])
				n_lines -= 1
		tot += n_lines
		print(b,p,n_lines)
	print(tot)
	run_tot += tot

print("Running total",run_tot)

print("##### Combined #####")
with open('limit_cycles_combined.txt','r') as f:
	lines = f.readlines()
	n_lines = len(lines)

	if lines[0][:2] == 'ID':
		n_lines -= 1

print("Combined lines:",n_lines)
