import random

secret = random.randint(1, 100)
numberOfGuesses = 0
while True:
        numberOfGuesses += 1 # +- er syntax for at variablen numberOfGuesses skal øke med 1
        print('This is guess number ' + str(numberOfGuesses))
        guess = int(input('Guess a number: '))
        if guess < secret:
                print('Too small')
        elif guess > secret:
                print('Too large')
        else:
                print('Correct! You spent ' + str(numberOfGuesses) + ' guesses')
                break
    
