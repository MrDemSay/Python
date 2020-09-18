
import math
import matplotlib.pyplot as plt
import numpy as np

file = open('data.txt', 'w')

def func():
	q = 0 #iterator
	i = 0 #iteraror


	R = 8.31
	M = 0.029
	g = 9.81
	P0 = 100000
	K = 1.4
	R_AIR = 287
	MU_0 = 18.27
	T_0 = 291.15
	C = 120

	t = 20;
	T = 0;
	h = 0;
	r = 25;

	while(q < r):
		q = q + 1


		t = t - 6
		T = t + 273
		h = h + 1

		p = P0 * math.exp((-M * g * h) / (R * T))
		po = (p * M) / (T * R)
		a = math.sqrt(K * R_AIR * T) #air_speed
		MU = MU_0 * ((T_0 + C) / (T + C)) * (T / T_0) ** (3 / 2) #viscosity

		i = i + 1

		file.write(str(h))
		file.write(' ')
		file.write(str(t))
		file.write(' ')
		file.write(str(round(p, 2)))
		file.write(' ')
		file.write(str(round(po, 2)))
		file.write(' ')
		file.write(str(round(a, 2)))
		file.write(' ')
		file.write(str(round(MU, 2)))
		file.write(' ')
		file.write('\n')
func()

file.close()



