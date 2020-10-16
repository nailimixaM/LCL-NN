'''
fi_1 = open('SLCL_1/limit_cycles_1_normalised.txt','r')
fi_2 = open('SLCL_2/limit_cycles_2_normalised.txt','r')
fo = open('limit_cycles_combined.txt','w')

line = fi_1.readline()
while line:
	fo.write(line)
	line = fi_1.readline()

line = fi_2.readline()
line = fi_2.readline()
while line:
	fo.write(line)
	line = fi_2.readline()

fi_1.close()
fi_2.close()
fo.close()

'''
fi_1 = open('GLCL_1/limit_cycles_1_to_6.txt','r')
fi_2 = open('GLCL_2/limit_cycles_2_to_6.txt','r')
fi_3 = open('GLCL_3/limit_cycles_3_to_6.txt','r')
fi_4 = open('GLCL_4/limit_cycles_4_to_6.txt','r')
fi_5 = open('GLCL_5/limit_cycles_5_to_6.txt','r')

'''
fi_1 = open('GLCL_1/limit_cycles_1_normalised.txt','r')
fi_2 = open('GLCL_2/limit_cycles_2_normalised.txt','r')
fi_3 = open('GLCL_3/limit_cycles_3_normalised.txt','r')
fi_4 = open('GLCL_4/limit_cycles_4_normalised.txt','r')
fi_5 = open('GLCL_5/limit_cycles_5_normalised.txt','r')
'''

fo = open('limit_cycles_combined.txt','w')

line = fi_1.readline()
while line:
	fo.write(line)
	line = fi_1.readline()

line = fi_2.readline()
line = fi_2.readline()
while line:
	fo.write(line)
	line = fi_2.readline()

line = fi_3.readline()
line = fi_3.readline()
while line:
	fo.write(line)
	line = fi_3.readline()

line = fi_4.readline()
line = fi_4.readline()
while line:
	fo.write(line)
	line = fi_4.readline()

line = fi_5.readline()
line = fi_5.readline()
while line:
	fo.write(line)
	line = fi_5.readline()

fi_1.close()
fi_2.close()
fi_3.close()
fi_4.close()
fi_5.close()

fo.close()
