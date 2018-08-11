#!/bin/python3

import math
import os
import random
import re
import sys



arr = list(map(int, input().rstrip().split()))
a=[]
for i in range (len(arr)):
    a.append(input().rstrip().split())

for j in range(arr[0]-1,-1,-1):
    print(int(a[0][j]),"",end="")
  
