lst = [int(l) for l in input().split()]
row_size, col_size, lst = lst[0], lst[1], []

for row in range(row_size):
    l = [int(l) for l in input().split()]
    for col in range(len(l), col_size, -1):
        l.remove(l[-1])
    lst.append(l)
    del l

print(lst)
