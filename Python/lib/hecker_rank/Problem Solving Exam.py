#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    result = []
    for username in usernames:
        new_user = list(username)
        found = 'NO'
        for i in range(len(username)):
            for j in range(i+1, len(username)):
                temp = new_user[i]
                new_user[i] = new_user[j]
                new_user[j] = temp
                user = ""
                for usr in new_user:
                    user += usr
                if user < username:
                    found = 'YES'
                    break
            if found == 'YES':
                break
        result.append(found)
    if 'NO' in result:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
