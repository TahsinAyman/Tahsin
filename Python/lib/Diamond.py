n = int(input('Enter the Value of Diamond: '))

for i in range(n):
    for y in range(n - 1, i, -1):
        print('  ', end='')
    for z in range(i * 2 + 1):
        print('*', end=' ')
    print()

for i in range(n - 1, 0, -1):
    for y in range(i, n):
        print('  ', end='')
    for z in range(i * 2 - 1, 0, -1):
        print('*', end=' ')
    print()
