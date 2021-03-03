#Attempt at Al Sweigart Rock Paper Scissors short program

import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0
numberOfTries = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties!')
    if numberOfTries > 0 :
        break
    else : 
        pass
    while True:
        print("Enter your move : (r)ock (p)aper (s)cissors or (q)uit")
        humanChoice = input()
        if humanChoice == 'q':
            sys.exit()
        elif humanChoice == 'r' or humanChoice == 'p' or humanChoice == 's':
            break
        else:
            print("Please type one of the following : p, q, r, s")
            True

    # computer's choice
    choices = ['r','p','s']
    computerChoice = choices[random.randint(0,2)]

    print("{} versus...".format(humanChoice))
    print("{}!".format(computerChoice))

    if humanChoice == 'r' and computerChoice == 's':
        wins += 1
        print("You won!")
    elif humanChoice == 'r' and computerChoice == 'p':
        losses += 1
        print("You lost!")
    if humanChoice == 'p' and computerChoice == 'r':
        wins += 1
        print("You won!")
    elif humanChoice == 'p' and computerChoice == 's':
        losses += 1
        print("You lost!")
    if humanChoice == 's' and computerChoice == 'p':
        wins += 1
        print("You won!")
    elif humanChoice == 's' and computerChoice == 'r':
        losses += 1
        print("You lost!")
    elif humanChoice == computerChoice :
        ties += 1
        print("It's a tie!")
    numberOfTries += 1