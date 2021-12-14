def calc(lst):
    sum = 0
    for i in lst:
        sum += i

    return f'>: = {sum}'


add = [int(inp) for inp in input('>: ').split(' + ')]
print(calc(add))
