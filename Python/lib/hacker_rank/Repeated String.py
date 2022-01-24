#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    cnt = 0
    string = s
    for i in range(n):
        s += string
    s = s[:n]
    for i in range(s):
        if 'a' == s[i]:
            cnt += 1
    return cnt


if __name__ == '__main__':
    s = input()
    n = int(input().strip())

    print(repeatedString(s, n))
