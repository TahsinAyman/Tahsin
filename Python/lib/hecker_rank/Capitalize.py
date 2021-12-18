#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    s = s.split()
    first_name = s[0]
    last_name = s[1]

    first_name = first_name[0].upper()
    last_name = last_name[0].upper()

    print(s)
    print(first_name)
    print(last_name)


name = input()
solve(name)
