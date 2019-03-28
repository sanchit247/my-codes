#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.

def climbingLeaderboard(scores, alice):
    position = []
    scores = list(dict.fromkeys(scores))
    extraElement = alice[0]
    scores.append(extraElement)
    lastAddedElementIndex = len(scores) - 1
    lastScore = alice[0]
    count = 0
    for aliceScore in alice:
        flag = 0
        
        if lastScore == aliceScore and count != 0:
            position.append(lastAddedElementIndex + 1)
            continue
        count = 1
        startIndex = lastAddedElementIndex
        endIndex = 0
        mid = (startIndex + endIndex)//2
        if aliceScore >= scores[mid]:startIndex = mid
        else : endIndex = mid 
        for j in range(startIndex,endIndex -1 , -1):
            if aliceScore >= scores[j] and (aliceScore < scores[j-1] or j == 0):
                scores.pop(lastAddedElementIndex)
                scores.insert(j,aliceScore)
                lastAddedElementIndex = j 
                flag = 1
                position.append(j + 1)
                break
            flag = 0
        if flag == 0:
            scores.pop(lastAddedElementIndex)
            scores.insert(len(scores),aliceScore)
            lastAddedElementIndex = len(scores) - 1
            position.append(lastAddedElementIndex + 1)
        lastScore = aliceScore
    return position


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
