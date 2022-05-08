n = int(input('Enter value of right side stairs: '))

for i in range(1, n + 1):
    for y in range(i, n):
        print('', end='  ')
    print('* ' * i)
