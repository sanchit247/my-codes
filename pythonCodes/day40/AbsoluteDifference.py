#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code herere
    count = 1
    newAr = {}
    tempAr = []
    a.sort()
    for i in range (0,len(a)):
        tempAr.append(a[i])
        kFlag = 0
        for j in range (0,len(a)):
            if i != j :
                if abs(a[i] - a[j]) == 0 or abs(a[i] - a[j]) == 1 : 
                    # checking that new number has 1 or 0 abs value
                    for k in range(0,len(tempAr)):
                         if abs(tempAr[k] - a[j]) == 0 or abs(tempAr[k] - a[j]) == 1 : 
                             kFlag = 0
                         else : 
                             kFlag = 1
                             break
                    if kFlag == 0 : tempAr.append(a[j]) 
        if len(tempAr) > count : count = len(tempAr)
        tempAr.clear()
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
