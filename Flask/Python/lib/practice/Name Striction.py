name = str(input('Enter your Name: '))

if len(name) < 3:
    print('Must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a Maximum of 50 characters')
else:
    print('Name looks good!')
