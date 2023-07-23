#python program to create matrix using numpy
import numpy as np
#Creating matrix using numpy.array
mat = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(mat)
print()

#Create matrix using numpy.array
mat = np.matrix("10 20 30;40 50 60;70 80 90")
print(mat)
print()

#another way to create a mtrix
mat = np.zeros((3,3), dtype= int)
print(mat)



