def assending_sort(lst):
    result = []
    for y in range(len(lst)):
        min = 0
        for i in range(len(lst)):
            if i == 0:
                min = lst[i]
            if lst[i] > min:
                max = lst[i]
        lst.remove(min)
        result.append(max)
    return result