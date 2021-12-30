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


def pyramid(n):
    for i in range(n):
        for y in range(n - 1, i, -1):
            print('  ', end='')
        for z in range(i * 2 + 1):
            print('*', end=' ')
        print()


def star(n):
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


print('1. Left side Stairs')
print('2. Right side Stairs')
print('3. Pyramid')
print('4. Star')
print('5. Box\n')

choice = int(input('Enter the choice: '))
n = int(input('Enter the Value: '))

if choice == 1:
    left_side_stair(n)
elif choice == 2:
    right_side_stair(n)
elif choice == 3:
    pyramid(n)
elif choice == 4:
    star(n)
elif choice == 5:
    box(n)
else:
    print('Wrong Choice')
