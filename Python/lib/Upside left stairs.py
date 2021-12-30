n = int(input('Enter the Value of Stairs: '))

for i in range(n + 1, 1, -1):
    for y in range(i, n + 1):
        print('  ', end='')
    for z in range(i - 1):
        print('*', end=' ')
    print()
