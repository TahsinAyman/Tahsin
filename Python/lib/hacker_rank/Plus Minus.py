#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = int()
    negative = int()
    zero = int()
    n = len(arr)

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1
    print("{0:.6f}".format(positive / n) + "\n" + "{0:.6f}".format(negative / n) + "\n" + "{0:.6f}".format(zero / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
