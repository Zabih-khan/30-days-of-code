
import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    m=[]
    for _ in range(6):
        arr.append(list(map(int, input("Enter NO:").rstrip().split())))
        for i in range(len(arr)-2):
            for j in range(len(arr)-2):
                #This line for a b c
               m.append(sum([arr[i][j],arr[i][j+1],arr[i][j+2],
                #This for d            
                arr[i+1][j+1],
                #This for e f g
                arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]))     
    print(max(m))
