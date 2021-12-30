n = int(input('Enter Stair Value: '))

for i in range(n):
    for y in range(i, n-1):
        print('  ', end='')

<<<<<<< HEAD
    for z in range(i + 1):
        print('* ', end='')
    print('')
=======
# Start

for row in range(1, int(input('Enter the Value of stairs: ')) + 1):
    print('* ' * row)

# End
>>>>>>> 768734806ea72e6f2c6780fe12a8740f0d0463e5
