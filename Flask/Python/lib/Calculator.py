from msvcrt import getch
from os import system
from lib.calculator.addition import add
from lib.calculator.subtraction import sub
from lib.calculator.multiiplication import multi
from lib.calculator.division import div


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
