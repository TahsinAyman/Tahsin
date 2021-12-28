from ishaan import ishaan
from Tahsin import *

# Please Test others Assignment here
while True:
    print('0. Exit')
    print('1. Tahsin Ayman')
    print('2. Asadunnobie Ishaan')
    print('3. Prottoy')
    print('4. Golpo')
    print('5. Anjum')

    choice = input('Enter your choice: ')

    if choice == '1' or choice == 'Tahsin':
        print("1. Tahsin's first assignment")
        print("2. Tahsin's second assignment")
        choice = int(input('Enter Choice(Integer)'))
        if choice == 1:
            tahsin_1()
        elif choice == 2:
            tahsin_2()
        else:
            print('Wrong choice')
    elif choice == '2' or choice == 'Ishaan':
        ishaan()
    elif choice == '3' or choice == 'Prottoy':
        pass
    elif choice == '4' or choice == 'Golpo':
        pass
    elif choice == '5' or choice == 'Anjum':
        pass
    elif choice == '0' or choice == 'Exit':
        exit('BYE')
    else:
        print('Wrong choice')

