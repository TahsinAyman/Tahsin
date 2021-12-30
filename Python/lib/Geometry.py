from time import sleep


def basic_box(n):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print('*', end=' ')
        print()


def upside_pyramid(n):
    for i in range(n - 1, 0, -1):
        for y in range(i + 1, n):
            print('  ', end='')
        for z in range(i * 2 - 1, 0, -1):
            print('*', end=' ')
        print()


def upside_right_stairs(n):
    for i in range(n + 1, 1, -1):
        for y in range(i, n + 1):
            print('  ', end='')
        for z in range(i - 1):
            print('*', end=' ')
        print()


def upside_left_stairs(n):
    for row in range(n + 1, 1, -1):
        for col in range(row - 1, 0, -1):
            print('*', end=' ')
        print()


def left_side_stair(n):
    for i in range(1, n + 1):
        for y in range(1, i + 1):
            print('*', end=' ')
        print()


def right_side_stair(n):
    for i in range(n):
        for y in range(n - 1, i, -1):
            print('  ', end='')
        for z in range(i + 1):
            print('*', end=' ')
        print()


def pyramid(n):
    for i in range(n):
        for y in range(n - 1, i, -1):
            print('  ', end='')
        for z in range(i * 2 + 1):
            print('*', end=' ')
        print()


def diamond(n):
    for i in range(n):
        for y in range(n - 1, i, -1):
            print('  ', end='')
        for z in range(i * 2 + 1):
            print('*', end=' ')
        print()

    for i in range(n - 1, 0, -1):
        for y in range(i, n):
            print('  ', end='')
        for z in range(i * 2 - 1, 0, -1):
            print('*', end=' ')
        print()


def box(n):
    print('╔', end=' ')
    for top in range(1, (n // 2) + 2):
        print('═', end=' ')
    print('╗')

    for row in range(1, (n // 2) + 2):
        print('║', end='')
        for col in range(1, (n // 2) + 2):
            print('  ', end='')
        print(' ║', end='')
        print()

    print('╚', end=' ')
    for bottom in range(1, (n // 2) + 2):
        print('═', end=' ')
    print('╝', end=' ')


def main():
    global n
    while True:
        print('')
        print('0. Exit                   5. Pyramid')
        print('1. Left Side Stair        6. Upside Pyramid')
        print('2. Right Side Stair       7. Basic Box')
        print('3. Upside Right Stairs    8. Box')
        print('4. Upside Left Stairs     9. Diamond\n')

        choice = input('Enter the choice: ')
        choice = choice.lower()

        if choice == '0':
            break
        else:

            if choice == '1' or choice == 'left side stair':
                n = int(input('Enter the Value: '))
                left_side_stair(n)
            elif choice == '2' or choice == 'right side stair':
                n = int(input('Enter the Value: '))
                right_side_stair(n)
            elif choice == '3' or choice == 'upside right stairs':
                n = int(input('Enter the Value: '))
                upside_right_stairs(n)
            elif choice == '4' or choice == 'upside left stairs':
                n = int(input('Enter the Value: '))
                upside_left_stairs(n)
            elif choice == '5' or choice == 'pyramid':
                n = int(input('Enter the Value: '))
                pyramid(n)
            elif choice == '6' or choice == 'upside pyramid':
                n = int(input('Enter the Value: '))
                upside_pyramid(n)
            elif choice == '7' or choice == 'basic box':
                n = int(input('Enter the Value: '))
                basic_box(n)
            elif choice == '8' or choice == 'box':
                n = int(input('Enter the Value: '))
                box(n)
            elif choice == '9' or choice == 'diamond':
                n = int(input('Enter the Value: '))
                diamond(n)
            else:
                print('Wrong Choice')

    for ch in 'Thank You':
        print(ch, end='')
        sleep(0.30)


main()
