n = int(input('Enter value of Pyramid: '))

for i in range(n):
    for y in range(n - 1, i, -1):
        print(' ', end='')
    for z in range(i * 2 + 1):
        print('*', end='')
    print()
