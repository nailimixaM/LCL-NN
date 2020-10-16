import numpy as np

def calc_area(dx, y):

	n_area = x.shape[0] - 1
	a = np.empty(n_area)


	for i in range(n_area):
		r1, r2 = y[i], y[i+1]
		a[i] = np.pi*(r1+r2)*np.sqrt(dx**2 + (r1-r2)**2)

	print(a)
	print(np.sum(a))


x = np.arange(10)
y = np.arange(10)[::-1]

calc_area(1,y)

a1 = np.pi*y[0]*np.sqrt(x[-1]**2 + y[0]**2)
print(a1)
