n = int(input('Enter Stair Value: '))

for row in range(1, n + 1):
    for col in range(row, n):
        print('  ', end='')
    print('* ' * row)
