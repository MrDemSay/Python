import math
import numpy as np

file = open('data.txt', 'w')

h = 0.2
pogr = 0
q = 0
i = 0
p = 1.5
Y = [1.5]
YG = []
YM = []
X = [0]


def func1(h, q, i, p):
	while (i <= 3):
		
		y = p + h * (p-q)
		
		q = q + 0.2
		
		yg = 0.5 * math.exp(q) + q + 1

		ym = p + h/2 * ((p-q) + ((h * (p-q) + p - (q+0.2))))

		p = y


		X.append(round(q, 3))
		Y.append(round(y, 3))
		YG.append(round(yg, 3))
		YM.append(round(ym, 3))


		file.write(str(round(y, 3)))
		file.write(' ')
		file.write(str(round(q, 3)))
		file.write(' ')
		file.write(str(round(yg, 3)))
		file.write(' ')
		file.write(str(round(q, 3)))
		file.write(' ')
		file.write(str(round(ym, 3)))
		file.write(' ')
		file.write(str(round(q, 3)))
		file.write(' ')
		file.write('\n')

		i = i + 1

func1(h, q, i, p)
print(X, end="\n")
print(Y, end="\n")
print(YG, end="\n")
print(YM, end="\n")

file.close()
