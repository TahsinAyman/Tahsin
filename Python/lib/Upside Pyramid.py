n = int(input('Enter the Value of Pyramid: '))

for i in range(n - 1, 0, -1):
    for y in range(i + 1, n):
        print('  ', end='')
    for z in range(i * 2 - 1, 0, -1):
        print('*', end=' ')
    print()
