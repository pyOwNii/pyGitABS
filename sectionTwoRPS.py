import random
import sys

print('Rock, Paper, Scissors')

#Keeping track of wins, loss and ties.
wins = 0
losses = 0
ties = 0

#we need an infinite loop to keep the game running
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #Player input loop.
        print('Enter your move (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quits
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Break out of the player input loop
        print('Type one of r, p, s, or q')


        #display what player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    if playerMove == 'p':
        print('PAPER versus...')
    if playerMove == 's':
        print('SCISSORS versus...')

        #display what computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

        #display and record the win/loss/tie
    if playerMove == computerMove:
        print('it is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose')
        losses = losses + 1