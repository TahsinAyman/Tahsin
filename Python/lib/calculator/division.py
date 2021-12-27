def div(lst):
    result = float()
    for integer in lst:
        if integer == lst[0]:
            result = integer
        else:
            result = result / integer
    return '>: = {0:.2f}'.format(result)
