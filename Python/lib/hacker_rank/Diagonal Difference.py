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

"""
3
1 2 3
4 5 6
7 8 9
=====
1 + 5 + 9 = 15
3 + 5 + 7 = 15
15 - 15 = 0
:param arr:
:return:
"""


def diagonalDifference(arr):
    cnt = len(arr)
    diagonal_sum = 0
    diagonal_sum_upside = 0

    for y in range(len(arr)):
        diagonal_sum += arr[y][y]

    for i in range(len(arr)):
        cnt = cnt - 1
        for z in range(cnt, -1, -1):
            diagonal_sum_upside += arr[i][z]
            i = i + 1
        break

    if diagonal_sum > diagonal_sum_upside:
        return diagonal_sum - diagonal_sum_upside
    else:
        return diagonal_sum_upside - diagonal_sum


if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))
