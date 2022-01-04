#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    result = str()
    for i in range(len(a) - 1, -1, -1):
        result += str(a[i]) + ' '
    return result


if __name__ == '__main__':
    n = int(input())
    arr = [int(l) for l in input().split()]
    print(reverseArray(arr))
