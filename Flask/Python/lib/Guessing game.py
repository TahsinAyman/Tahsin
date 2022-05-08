from random import random

random_limit = int(input('Enter your random limit: '))
secret_number = int(random() * random_limit)
guess_count = 0
guess_limit = int(input('Enter your limit: '))
# print(secret_number)

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
    else:
        print('Noob')
