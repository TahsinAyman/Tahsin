choice = int(input('Enter your choice: '))
is_hot = bool()
is_cold = bool()

if choice == 0:
    is_hot = True
elif choice == 1:
    is_cold = True
else:
    print('Wrong choice')
    quit()

if not is_hot:
    is_cold = True
elif not is_cold:
    is_hot = True

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
