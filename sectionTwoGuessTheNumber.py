#Guess the number

import random
randomNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#Ask the player to guess 7 times
for guessTaken in range(1,8):
    print('Take a guess')
    guess = int(input())

    if guess < randomNumber:
        print('Your guess is too low')
    elif guess > randomNumber:
        print('Your guess is too high.')
    else:       #Else is used when correct number is hit
        break

if guess == randomNumber:
    print('Good, you guessed the random number in ' + str(guessTaken) + 'guesses')
else:
    print('Nope, wrong guesses, the random number was: ' + str(randomNumber))