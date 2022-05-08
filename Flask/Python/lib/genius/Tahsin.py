def tahsin_1():
    # Assignment in two ways
    # First Way:

    # The Way you teach (:

    # Start

    for row in range(1, int(input('Enter the Value of stairs: ')) + 1):
        print('* ' * row)

    # End


def tahsin_2():
    # Assignment in two ways
    # Second Way:

    # Start:

    # Didn't Teach us this way ):

    for row in range(1, int(input('Enter the Value of stairs: ')) + 1):
        for col in range(1, row + 1):
            print('*', end=' ')
        print('\n')

    # End

# Bonus Way
# for i in range(1, int(input('Enter Data: ')) + 1): print('* ' * i)
