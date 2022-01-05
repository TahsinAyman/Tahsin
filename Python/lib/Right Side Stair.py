n = int(input('Enter value of right side stairs: '))

for i in range(n):
    for y in range(n, i + 1, -1):
        print(' ', end='')
    print('* ' * i)
