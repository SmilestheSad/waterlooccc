#!/bin/python3

import math
import os
import random
import re
import sys


def getSum(x,y,arr):
    res = 0
    # print(x,y,x,y+1)
    res += arr[x][y]
    res += arr[x][y+1]
    res += arr[x][y+2]

    res += arr[x+1][y+1]
    res += arr[x+2][y]
    res += arr[x+2][y+1]
    res += arr[x+2][y+2]
    
    return res



if __name__ == '__main__':
    arr = []
    sumList = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for x in range(4):
        for y in range(4):
            res = getSum(x,y,arr)
            # print(x,y,res)
            sumList.append(res)
print(max(sumList))
