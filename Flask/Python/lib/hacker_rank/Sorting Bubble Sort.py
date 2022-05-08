#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count = int()
    cnt = 0
    for _ in range(len(a)):
        cnt += 1
        for i in range(len(a) - cnt):
            if a[i] > a[i + 1]:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                count += 1
    return count


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
