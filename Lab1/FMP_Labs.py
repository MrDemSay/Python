import math
import numpy as np

file = open('data.txt', 'w')

def Eilers_method(x, y_prev, h):
	file = open('EILERdata.txt', 'w')

	i = 0

	while (i <= 3):
		x = x + h
		y = y_prev + h * (y_prev-x)
		yg = 0.5 * math.exp(x) + x + 1
		ym = y_prev + h/2 * ((y_prev-x) + ((h * (y_prev-x) + y_prev - (x+0.2))))
		
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

	print("Eilers_method completed successfully...")





def RungeKutta_Method(x, y_prev, h):
	file = open('RKdata.txt', 'w')

	i = 0 #счётчик
	y = 0 #инициализация
	number_k_elements = 3 
	k_array = [] #для хранения и суммирования элементов k

	while (i <= number_k_elements and x <= 1):
		if i == 0:
			k = h * (2 * (x ** 2 + y_prev))
			k_array.append(k)

		elif i > 0 and i < number_k_elements:
			y = y_prev + 1/6 * sum(k_array)
			y_prev = y #переопределение значений

			k = h * (2 * ((x + h/2)**2 + (y + k_prev/2)))
			k_array.append(2 * k)

		else:
			y = y_prev + 1/6 * sum(k_array)
			y_prev = y #переопределение значений

			k = h * (2 * ((x + h) ** 2 + y + k_prev))
			k_array.append(k)

		

		#запись в файл
		file.write(str(round(k, 3)))
		file.write(' ') 
		file.write(str(round(x, 3)))
		file.write(' ')
		file.write(str(round(y_prev, 3)))
		file.write(' ')
		file.write('\n')


		k_prev = k #переопределение значений

		x = x + h #прибавляем шаг
		i = i + 1


	print("RungeKutta_Method completed successfully...")



Eilers_method(0, 1, 0.1)

RungeKutta_Method(0, 1, 0.1)


file.close()
