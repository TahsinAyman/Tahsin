n = int(input('Enter Stair Value: '))

for i in range(n):
    for y in range(i, n-1):
        print('  ', end='')

    for z in range(i + 1):
        print('* ', end='')
    print('')
