import math
import os
import random
import re
import sys


n = int(input().strip())

if n in range(1, 101):
    if (n % 2) != 0:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif n in range(6, 21):
        print('Weird')
    elif n > 20:
        print('Not Weird')
