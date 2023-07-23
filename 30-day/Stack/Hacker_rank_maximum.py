#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    print(max(operations))


# Write your code here


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input("How many..").strip())
    ops = []
    for _ in range(n):
        ops_item = input("Enter...")
        ops.append(ops_item)
    getMax(ops)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
