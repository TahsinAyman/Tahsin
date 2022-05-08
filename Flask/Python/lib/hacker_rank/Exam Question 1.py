#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:

    def add(self, val):
        lst = [].append(val)
        pass

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return 0


if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result


    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    print(result)

# 12
# query 1
# add 1
# query 1
# remove 1
# query 1
# add 2
# add 2
# size
# query 2
# remove 2
# query 2
# size
