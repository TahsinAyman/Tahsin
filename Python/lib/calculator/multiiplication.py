def multi(lst):
    sum = float()
    for i in lst:
        if i == lst[0]:
            sum = i
        else:
            sum = sum * i
    print('>: = ', '{0:.2f}'.format(sum))

