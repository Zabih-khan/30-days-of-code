#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("How many number you want to enter:").strip())
    a=[]
    for i in range(n):
        x=int(input("Enter number"))
        a.append(x)
##        a = list(map(int, input("Enter all Number in sequence:").rstrip().split()))
    count=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                count+=1            
    print("Array is sorted in ",(count),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
