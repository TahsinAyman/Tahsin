n = int(input('Enter the Value of Left Side Stairs: '))

for i in range(1, n + 1):
    for y in range(1, i + 1):
        print('*', end=' ')
    print()
