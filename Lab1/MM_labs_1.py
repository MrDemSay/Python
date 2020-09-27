import math
import numpy as np

file = open('data.txt', 'w')


def func1(h, q, i, p):

	h = 0.2
	pogr = 0
	q = 0
	i = 0
	p = 1.5
	Y = [1.5]
	YG = []
	YM = []
	X = [0]

	while (i <= 3):
		q = q + 0.2
		y = p + h * (p-q)
		yg = 0.5 * math.exp(q) + q + 1
		ym = p + h/2 * ((p-q) + ((h * (p-q) + p - (q+0.2))))
		
		p = y

		X.append(round(q, 3))
		Y.append(round(y, 3))
		YG.append(round(yg, 3))
		YM.append(round(ym, 3))

		#recording in file 
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

def RungeKutta():

	Y_ = [1]
	X_ = [0]
	K_ = []
	i = 0
		

	H = 0.1

	while(i < 4):

		if i == 0:
			K_[i] = H * (2 * (X_[i] ** 2 + Y_[i]))
			K_.append(K_[i])
			
		elif(i > 0 and len(K_) < 3):
			X_[i] = X_[x-1] + H
			K_[i] = H * ((X_[i] + H/2) ** 2 + Y_[i] + K_[i-1]/2)
			K_.append(K_[i])
		else:
			K_[i] = H * 2 * ((X_[i]+H)**2 + Y_[i]+K_[i-1])
			K_.append(K_[i])


		
		
		X_.append(X_[i])

		Y_[i+1] = Y_[i] + 1/6*(K_[0] + 2*K_[1] + 2*K_[2] + K_[3])
		Y_.append(Y_[i+1])


		i = i + 1
		

		

		



#func1(h, q, i, p)

RungeKutta()
print("X_ARRAY: ", X_, end="\n")
print("Y_ARRAY: ", Y_, end="\n")
print("K_ARRAY: ", K_, end="\n")


#arrays
#print(X, end="\n")
#print(Y, end="\n")
#print(YG, end="\n")
#print(YM, end="\n")

file.close()
