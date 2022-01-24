def div(lst):
    sum = float(lst[0])
    for i in range(1, len(lst)):
        sum = sum / lst[i]
    print('>: = ', '{0:.2f}'.format(sum))
