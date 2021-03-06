#Attempt at Al Sweigart Rock Paper Scissors short program

import random, sys

print('READY...SET...GO! ROCK, PAPER, SCISSORS!')

wins = 0
losses = 0
ties = 0
moves = {'r':'Rock','p':'Paper','s':'Scissors'}
# numberOfTriesAllowed = 0 

while True: # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties!')
    """Used if a limited number of rounds need to be established
    if numberOfTriesAllowed == 3 :
        break
    else : 
        pass """
    while True: # The player input loop.
        print("Enter your move : (r)ock (p)aper (s)cissors or (q)uit")
        humanChoice = input()
        if humanChoice == 'q':
            sys.exit()
        elif humanChoice == 'r' or humanChoice == 'p' or humanChoice == 's':
            break
        else:
            print("Please type one of the following : p, q, r, s")

    # computer's choice
    computerChoice = random.choice(list(moves.keys()))

    print("Player's {} versus...".format(moves[humanChoice]))
    print("Computer's {}!".format(moves[computerChoice]))

    # outcome of the match
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
    #numberOfTriesAllowed += 1