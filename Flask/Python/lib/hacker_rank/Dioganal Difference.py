#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    cnt = 0
    sum = []
    for i in arr:
        sum.append(i[cnt])
        cnt += 1
    left_right_sum = 0
    for i in sum:
        left_right_sum += i
    cnt = len(arr) - 1
    sum = []
    right_left_sum = 0
    for i in arr:
        sum.append(i[cnt])
        cnt -= 1
    for i in sum:
        right_left_sum += i
    if right_left_sum > left_right_sum:
        return right_left_sum - left_right_sum
    else:
        return left_right_sum - right_left_sum


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diagonalDifference(arr))
