def small_big_sort(lst):
    result = []
    for _ in range(len(lst)):
        max = lst[0]
        for i in range(len(lst)):
            if lst[i] < max:
                max = lst[i]
        lst.remove(max)
        result.append(max)
    del lst
    return result


def big_small_sort(lst):
    result = []
    for _ in range(len(lst)):
        min = lst[0]
        for i in range(len(lst)):
            if lst[i] > min:
                min = lst[i]
        lst.remove(min)
        result.append(min)
    del lst
    return result


lst = [int(l) for l in input().split()]
lst = small_big_sort(lst)
print(lst)
lst = big_small_sort(lst)
print(lst)
