from addition import add
from subtraction import sub
from multiiplication import multi
from division import div
from msvcrt import getch
from os import system


def Calculator():
    while 1:
        system('cls')
        print('0. Exit')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division\n')

        choice = int(input('Enter your Choice: '))

        if choice == 1:
            lst_add = [float(inp_add) for inp_add in input('Enter Number: ').split(' + ')]
            print('')
            add(lst_add)
            getch()
        elif choice == 2:
            lst_sub = [float(inp_sub) for inp_sub in input('Enter Number: ').split(' - ')]
            print('')
            sub(lst_sub)
            getch()
        elif choice == 3:
            lst_multi = [float(inp_multi) for inp_multi in input('Enter Number: ').split(' x ')]
            print('')
            multi(lst_multi)
            getch()
        elif choice == 4:
            lst_div = [float(inp_div) for inp_div in input('Enter Number: ').split(' / ')]
            print('')
            div(lst_div)
            getch()
        elif choice == 0:
            print('Thank you')
            getch()
            quit()
        else:
            print('')
            print('Error!')
            getch()
        print('')


Calculator()
