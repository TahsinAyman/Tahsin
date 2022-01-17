#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    lst = list(arr)
    result = []
    for i in range(len(lst)):
        lst.remove(lst[i])
        sum = 0
        for y in lst:
            sum += y
        result.append(sum)
        lst = list(arr)
    print(result[len(result) - 1], result[0])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

