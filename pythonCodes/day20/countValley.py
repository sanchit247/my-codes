#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count =0
    v=0
    for i in range(n):
        if(s[i]=="D"):count -=1
        if(s[i]=="U"):count+=1
        if(count==0 and s[i] == "U"):v+=1
    print(min,'--')
    return str(v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
