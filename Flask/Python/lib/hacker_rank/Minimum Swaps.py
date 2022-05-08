#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = int()
    cnt = 0
    for _ in range(len(arr)):
        cnt += 1
        for i in range(len(arr) - cnt):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                count += 1
    return count


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(minimumSwaps(arr))
