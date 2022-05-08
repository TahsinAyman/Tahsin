dic = {}

for i in range(3):
    lst = [int(l) for l in input().strip().split()]
    dic = {lst[0], lst[1]}
print(dic)
