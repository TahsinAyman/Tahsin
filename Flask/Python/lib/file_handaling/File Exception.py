from os import system

try:
    address = input('Write Address: ')

    f = open(address, 'r')
    text = f.read()
    print(text, end='')

    f.close()

    f = open(address, 'a')
    f.write(input(''))

    f.close()

    print('0. Exit')
    print('1. Delete everything exist in the file')
    print('2. Delete the file')

    choice = int(input())

    if choice == 1:
        system('del ' + address)
    elif choice == 0:
        f = open(address, 'w')
        f.close()
    elif choice == 2:
        exit('Noob')
except FileNotFoundError:
    print('File Not Find. The Address you typed were not found\nPlease, make sure to Create a file')
