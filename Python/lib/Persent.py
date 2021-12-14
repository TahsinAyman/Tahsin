price = 1000000
good_credit = bool()
choice = int(input('Enter your choice: '))

if choice == 0:
    good_credit = True
elif choice == 1:
    good_credit = False
else:
    print('Wrong choice')
    quit()

if good_credit:
    price = (price * 10) / 100
else:
    price = (price * 20) / 100

print('Total Price: ', price)
