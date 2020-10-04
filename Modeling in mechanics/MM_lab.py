 import math
 import numpy as np

 #variant 2

 def func():
 	h = 1.4
 	h2 = 1.8
 	h_c = h / 2
 	g = 9.81
 	gamma = ro * g 
 	a = 3
 	b = 3
 	S = a * b
 	p0 = 100000
 	#WATER = 1000
 	#PETROL = 700
 	#NEFT = 850
 	#KEROSINE = 820
 	#MOTOR OIL = 910
 	#ULFURIC_ACID = 1835

 	ro = [1000, 700, 850, 820, 910, 1835]

 	i = 0 
 	while i <= len(ro):
 		p = p0 + ro[i] * g * h/2
 		gamma = ro[i] * g 
 		F_vertical = gamma * V_t_d
 	 	F_horizontal = p_C * S_vertical
 	F_1 = sqrt(F_horizontal**2 + F_vertical**2) #сила гидростатического давления
 	F_2 = (p0 + ro[i] * g * h_c) * S  #абсолютное суммарное давление

