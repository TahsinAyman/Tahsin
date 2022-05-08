n = int(input('Enter the Value of Pyramid: '))

for i in range(n, 0, -1):
    for y in range(i + 1, n + 1):
        print('  ', end='')
    print('* ' * (i * 2 - 1))
