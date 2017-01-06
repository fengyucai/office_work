import random

n = random.randint(1, 20)
numOfGuess = 0
print('I am thinking of an integer between 1 and 20.')
print('Take a guess.')
while True:
    guess = int(input())
    numOfGuess += 1
    if guess == n:
        print('Good job! You guessed my number in ' + \
        str(numOfGuess) + ' guesses!')
        break
    print('Your guess is too ', end='')
    if guess < n:
        print('low.')
    else:
        print('high.')
    print('Take a guess:')
      


