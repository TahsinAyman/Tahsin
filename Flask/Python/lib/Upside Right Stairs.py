n = int(input('Enter the Value of Stairs: '))

for row in range(n + 1, 1, -1):
    for col in range(row - 1, 0, -1):
        print('*', end='')
    print()
