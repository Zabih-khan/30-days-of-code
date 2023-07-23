#Write a python program which take two digit m and n as inut and generate
#a two dimensional array. The element value in the i-th row and j-th colume
#of the array should be i*j
import numpy as np
row = int(input("Enter the number."))
col = int(input("Enter the number."))
x = [[i for i in range(row)]for j in range(col)]
print(x)
