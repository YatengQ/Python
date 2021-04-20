import numpy as np
import matplotlib as plt
import math

My_list = []
x = []
y = []
psi = []
Points = []
D = int(input("Please input the demension:"))

for num in range(0,D):
    x.append(num)
    y.append(num)
for num_x in x:
    for num_y in y:
        My_list.append((num_x,num_y))

def per(List):
    for num in range(0,len(List)):
        psi.append(math.sin(List[num][0])*math.sin(List[num][1]))
    return psi

T = np.array(per(My_list))
P = np.column_stack((My_list,T))

np.savetxt('Out100.txt', P, fmt="%.5f", delimiter=',')
