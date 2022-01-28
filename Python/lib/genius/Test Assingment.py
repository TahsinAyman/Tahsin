n, sum = int(input()), []
lst1 = [int(_) for _ in input().strip().split()]
lst2 = [int(_) for _ in input().strip().split()]
for i in range(n):
    sum.append(lst1[i] + lst2[i])
for i in sum:
    print(i, end=' ')

'''
5 5
1024
2048
7789
4321
42
0 2
0 7
0 3
1 3 1131
0 3

6
1 2 3 4 5 6
9 5 4 1 6 6

10 7 7 5 11
'''