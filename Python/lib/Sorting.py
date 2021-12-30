def sort(lst):
    tmp = []
    max = -1
    max2 = -1
    for z in lst:
        for i in lst:
            if max < i:
                max = i
                lst.remove(i)
                lst.insert(0, max)
            else:
                tmp.append(i)
    print(max)
    return lst


lst = [int(l) for l in input().split()]
print(sort(lst))
