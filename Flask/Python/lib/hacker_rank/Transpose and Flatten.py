import numpy

lst = [int(i) for i in input().split()]
N = lst[0]
M = lst[1]
del lst

for row in range(N):
    for col in range(M):
        lst = [int(i) for i in input().split()]
    print('')
