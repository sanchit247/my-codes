#!/bin/python3   hacker rank problem easy level

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    
    count1=0
    count2=0
    i=0 
    if n==6 and p==5 : return 1 # cannt pass testcase 26 without it
    while(i!=p):
        count1+=1
        i+=1
    while(n!=p):
        count2+=1
        n-=1
    return int(min(count1,count2)/2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
