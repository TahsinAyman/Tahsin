from msvcrt import getch
from os import system


def add():
    var1 = float(input('Enter the Number: '))

    while 1:
        var2 = float(input('Enter the Number: '))
        if var2 == 0:
            break
        var1 = var1 + var2
    print('Result = ', var1)
    system('pause')


def sub():
    var1 = float(input('Enter the Number: '))

    while 1:
        var2 = float(input('Enter the Number: '))
        if var2 == 0:
            break
        var1 = var1 - var2
    print('Result = ', var1)
    system('pause')

def multi():
    var1 = float(input('Enter the Number: '))

    while 1:
        var2 = float(input('Enter the Number: '))
        if var2 == 0:
            break
        var1 = var1 * var2
    print('Result = ', var1)
    system('pause')

def div():
    var1 = float(input('Enter the Number: '))

    while 1:
        var2 = float(input('Enter the Number: '))
        if var2 == 0:
            break
        var1 = var1 / var2
    print('Result = ', var1)
    system('pause')

def Calculator():
    while 1:
        system('cls')
        print('0. Exit')
        print('1. Add')
        print('2. Sub')
        print('3. Multi')
        print('4. Div\n')

        choice = int(input('Enter your Choice: '))

        if choice == 1:
            print('')
            add()
        elif choice == 2:
            print('')
            sub()
        elif choice == 3:
            print('')
            multi()
        elif choice == 4:
            print('')
            div()
        elif choice == 0:
            quit()
        else:
            print('')
            print('Error!')
            getch()
            system('cls')
        print('')

Calculator()
