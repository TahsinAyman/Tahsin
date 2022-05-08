n, sum = int(input()), []
lst1 = [int(_) for _ in input().strip().split()]
lst2 = [int(_) for _ in input().strip().split()]
for i in range(n):
    sum.append(lst1[i] + lst2[i])
for i in sum:
    print(i, end=' ')
# Tahsin Ayman
