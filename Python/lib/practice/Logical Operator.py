high_income = bool()
good_credit = bool()
choice_for_income = str(input('Enter your choice for high income: '))
choice_for_credit = str(input('Enter your choice for good income: '))

if choice_for_income == 'True':
    high_income = True
elif choice_for_income == 'True':
    high_income = False
else:
    print('Wrong choice')

if choice_for_credit == 'True':
    good_credit = True
elif choice_for_credit == 'False':
    good_credit = False
else:
    print('Wrong choice')

if high_income and good_credit:
    print('Eligible for Loan')
