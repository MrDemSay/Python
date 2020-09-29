import math
import numpy as np

file = open('data.txt', 'w')


def Eilers_method():
	file = open('EILERdata.txt', 'w')

	h = 0.2
	x = 0
	i = 0
	p = 1.5 
	Y = [1.5]
	YG = []
	YM = []
	X = [0]

	while (i <= 3):
		x = x + 0.2
		y = p + h * (p-x)
		yg = 0.5 * math.exp(x) + x + 1
		ym = p + h/2 * ((p-x) + ((h * (p-x) + p - (x+0.2))))
		
		p = y #переопределение значения


		#recording in arrays
		#X.append(round(x, 3)) 
		#Y.append(round(y, 3))
		#YG.append(round(yg, 3))
		#YM.append(round(ym, 3))

		#recording in file 
		file.write(str(round(y, 3)))
		file.write(' ')
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(yg, 3)))
		file.write(' ')
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(ym, 3)))
		file.write(' ')
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write('\n')

		i = i + 1




def RungeKutta_Method():
	file = open('RKdata.txt', 'w')

	h = 0.1
	x = 0
	i = 0
	y = 0
	p = 1 #y_prev
	e = 1
	k_array = []
	y_array = []

	while (i <= 3 and x <= 1):

		if i == 0:
			k = h * (2 * (x ** 2 + p))
		elif i > 0 and i < 3:
			y = p + 1/6 * sum_k(k_array)
			y_array.append(y)
			k = h * (2 *((x + h/2) ** 2 + y + k_prev/2))
		else:
			y = p + 1/6 * sum_k(k_array)
			k = h * ((x + h) ** 2 + y + k_prev)

		
		k_array.append(k)
		def sum_k(k_array):
			suma = 0
			for i in k_array:
				suma += i
			return suma

		print(sum_k(k_array))
		print("y-array = ",y_array)


		#recording in file
		file.write(str(round(k, 3)))
		file.write(' ') 
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(p, 3)))
		file.write(' ')
		file.write('\n')

		p = y
		k_prev = k
		x = x + h
		i = i + 1

	print(k_array)

#Eilers_method()

RungeKutta_Method()

#print("X_ARRAY: ", X_, end="\n")
#print("Y_ARRAY: ", Y_, end="\n")
#print("K_ARRAY: ", K_, end="\n")


#arrays
#print(X, end="\n")
#print(Y, end="\n")
#print(YG, end="\n")
#print(YM, end="\n")

file.close()
