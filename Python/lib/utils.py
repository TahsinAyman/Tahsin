def find_max(lst: list):
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max
