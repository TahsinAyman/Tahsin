n = int(input('Enter value of right side stairs: '))

for i in range(n + 1):
    for y in range(n, i, -1):
        print('  ', end='')
    print('* ' * i)
