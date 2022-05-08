#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    count = dict()
    for i in a:
        cnt = 0
        for y in a:
            if i == y:
                cnt += 1
        count[i] = cnt
    result = int()
    for i in count:
        if count[i] == 1:
            result = i
    return result


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))
