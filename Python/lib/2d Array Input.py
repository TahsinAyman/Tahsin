# Input
n1 = int(input())
n2 = int(input())
lst = []
for row in range(n1):
    arr = [int(l) for l in input().split()]
    lst.append(arr)
del arr
# Output
print(lst)
