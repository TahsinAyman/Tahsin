x = int(input('Enter Data to start: '))
y = int(input('Enter Data to loop: '))
choice = str(input('Enter choice (Even or Odd): '))

for i in range(x, y+1):
    if choice == 'Even':
        if i % 2 == 0:
            print(i)
    elif choice == 'Odd':
        if i % 2 != 0:
            print(i)
    else:
        print('Wrong choice!')
