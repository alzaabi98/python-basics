'''
hint :
- import random
- to get random number use random.randnint(a,b)
- to get user input use input() funciton
- use for loop with range(0,5)
- use break
'''

import random


def guessGame():
    secretNum = random.randint(1, 20)
    print('I have secret number(1-20) , can you guess ?')

    for guessNum in range(0, 5):
        print('what is the number ?')
        guess = int(input())

        if guess < secretNum:
            print('your number is smaller than my number')
        elif guess > secretNum:
            print('your number is larger than my number')
        else:
            break

    if guess == secretNum:
        print(f'your number is correct- mine was {secretNum}')
    else:
        print(f'Please try again- mine was {secretNum}')


guessGame()
