import os
import time
import psutil


def tree(x, y):
    lst[x][y] = '|'
    if x-1 >= 0:
        lst[x-1][y] = '*'
        if y+1 < len(lst[x]):
            lst[x-1][y+1] = '*'
        if y+2 < len(lst[x]):
            lst[x-1][y+2] = '*'
        if y-1 >= 0:
            lst[x-1][y-1] = '*'
        if y-2 >= 0:
            lst[x-1][y-2] = '*'
        if y+2 < len(lst[x]):
            lst[x-1][y+2] = '*'
    if x-2 >= 0:
        lst[x-2][y] = '*'
        if y+1 < len(lst[x]):
            lst[x-2][y+1] = '*'
        if y-2 >= 0:
            lst[x-2][y-1] = '*'
    if x-3 >= 0:
        lst[x-3][y] = '*'


def home(r, c):
    lst[r][c] = '_'
    if c-1 >= 0:
        lst[r][c-1] = '|'
    if c+1 < len(lst[r]):
        lst[r][c+1] = '|'
    if r-1 >= 0:
        lst[r-1][c] = '_'
        if c-1 >= 0:
            lst[r-1][c-1] = '/'
        if c+1 < len(lst[r]):
            lst[r-1][c+1] = '\\'
    if r-2 >= 0:
        lst[r-2][c] = '_'


def init():
    for i in range(len(lst)):
        for y in range(len(lst[i])):
            if lst[i][y] == 2:
                tree(i, y)
            elif lst[i][y] == 3:
                home(i, y)
            elif lst[i][y] == 0:
                lst[i][y] = ' '
            elif lst[i][y] == 1:
                lst[i][y] = '#'
    for i in lst:
        for y in i:
            print(y, end='')
        print()


lst = []
for _ in range(list(map(int, input().strip().split()))[0]):
    lst.append(list(map(int, input().strip().split())))

start = time.time()
init()
done = time.time()
print((done - start)*1000)
process = psutil.Process(os.getpid())
print(process.memory_info().rss / 1024 ** 2)  # in bytes
'''
4 8
0 0 3 0 1 0 0 3 
0 0 0 3 0 0 0 0 
0 0 0 0 1 2 3 0 
0 0 0 0 0 0 1 0

9 16
0 0 0 3 0 0 0 0 0 1 0 0 0 3 0 0 
0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 2 0 3 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 3 0 0 0 0 0 
0 0 0 2 0 0 1 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 
0 0 0 2 0 3 0 0 0 0 0 0 0 0 0 3

16 16
0 0 0 3 0 0 0 0 0 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 2 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 3 0 0 0 0 0 
0 0 0 2 0 0 1 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 
0 0 0 2 0 3 0 0 0 0 0 0 0 0 0 3 
0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 
1 0 0 0 0 2 0 0 0 0 0 0 1 0 0 0 
2 0 0 0 3 0 0 1 0 0 3 0 0 1 0 0 
0 0 0 0 1 0 0 0 0 0 0 0 0 3 0 0

15 12
0 0 0 0 0 3 1 2 0 0 3 0 
0 0 0 0 0 0 0 0 0 0 0 0 
3 1 0 0 0 0 0 0 0 0 0 1 
0 0 0 0 1 0 0 0 0 0 1 0 
2 0 0 0 0 0 0 3 0 0 0 2 
0 0 0 2 0 0 0 0 0 0 0 0 
0 0 0 0 2 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 1 0 
0 0 3 0 0 0 0 0 3 0 0 0 
0 0 0 1 0 0 0 0 2 0 0 1 
0 0 0 0 0 0 0 0 3 0 0 0 
1 0 0 0 3 0 1 0 0 0 0 2 
1 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 3 0 0 0 3 0 0 0 0 
0 0 0 0 0 0 0 0 3 0 1 1
'''