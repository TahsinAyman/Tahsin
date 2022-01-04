def sort(lst, order='asc'):  # 1 3 2 4
    result = []
    for _ in range(len(lst)):
        max = lst[0]
        for i in range(len(lst)):
            if order == 'asc':
                if lst[i] < max:
                    max = lst[i]
            elif order == 'desc':
                if lst[i] > max:
                    max = lst[i]
            else:
                return 0
        lst.remove(max)
        result.append(max)
    return result


lst = [int(l) for l in input().split()]
lst = sort(lst)
print(lst)
