n = int(input('Enter value of right side stairs: '))

for i in range(n):
    for y in range(n - 1, i, -1):
        print('  ', end='')
    for z in range(i + 1):
        print('*', end=' ')
    print()
