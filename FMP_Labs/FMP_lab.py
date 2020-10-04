import numpy as np
import pandas as pd
import math

# a = [0.1, 0.2, 0.3, 0.4, 0.5]
# b = [1,2,3,4,5]
# c = [10, 20, 30, 40, 50]
# data = {'y':b, 'z':c}

# f = pd.DataFrame(data, index=a)

# print(f)




file = open('data.txt', 'w')

def Eilers_method(x, y_prev, h):
	file = open('EILERdata.txt', 'w')
	f = open('Eilers_table.txt', 'w')


	i = 0
	y_numbers = 3
	X_arr = [] #for building table 
	Y_arr = [] #for building table
	YG_arr = [] #for building table
	YM_arr = [] #for building table

	while (i <= y_numbers):
		x = x + h
		X_arr.append(round(x, 3))
		y = y_prev + h * (y_prev-x)
		Y_arr.append(round(y, 3))
		yg = 0.5 * math.exp(x) + x + 1
		YG_arr.append(round(yg, 3))
		ym = y_prev + h/2 * ((y_prev-x) + ((h * (y_prev-x) + y_prev - (x+0.2))))
		YM_arr.append(round(ym, 3))
		
		y_prev = y #переопределение значения


		#recording in file 
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(y, 3)))
		file.write(' ')
		file.write(str(round(yg, 3)))
		file.write(' ')
		file.write(str(round(ym, 3)))
		file.write(' ')
		file.write('\n')

		i = i + 1

	#output in table
	data = {'Y_Обычный':Y_arr, 'Y_Точный':YG_arr, 'Y_Модифицированный':YM_arr}
	fd = pd.DataFrame(data, index=X_arr)

	#recording table in file
	f.write(str(fd))
	f.close()

	print("Eilers_method completed successfully...")
	
	
	





def RungeKutta_Method(x, y_prev, h):
	file = open('RKdata.txt', 'w')
	f = open('Runge-Kutta_table', 'w')

	i = 0 #counter
	y = 0 #init
	k_prev = 0 #init
	number_k_elements = 3 #for input user
	k_array = [] #for save and sum k-elements
	K_table = [] #save data for table
	X_arr = []
	Y_arr = [y_prev]

	while (i <= number_k_elements):
		if i == 0:
			k = h * (2 * (x ** 2 + y_prev))
			k_array.append(round(k, 3))

		elif i > 0 and i < number_k_elements:
			y = y_prev + 1/6 * sum(k_array)
			Y_arr.append(round(y, 3))
			y_prev = y #redefine value

			k = h * (2 * ((x + h/2)**2 + (y + k_prev/2)))
			k_array.append(round(2 * k, 3))

		else:
			y = y_prev + 1/6 * sum(k_array)
			Y_arr.append(round(y, 3))
			y_prev = y #redefine value

			k = h * (2 * ((x + h) ** 2 + y + k_prev))
			k_array.append(round(k, 3))

		

		#recording in file
		file.write(str(round(k, 3)))
		K_table.append(round (k, 3))
		file.write(' ') 
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(y_prev, 3)))
		file.write(' ')
		file.write('\n')

		X_arr.append(round(x, 3))
		x = x + h #step up

		k_prev = k #redefine value
		i = i + 1 #counter

	#output in table
	data = {'Y_Обычный':Y_arr, 'K_значение':K_table}
	fd = pd.DataFrame(data, index=X_arr)


	#recording table in file
	f.write(str(fd))
	f.close()

		


	print("RungeKutta_Method completed successfully...")



Eilers_method(0, 1, 0.1)

RungeKutta_Method(0, 1, 0.1)


file.close()
