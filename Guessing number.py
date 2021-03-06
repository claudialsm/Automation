import random
secretNumber = random.randint(1,5)

print('I am thinking of a number between 1 and 10')
# ask the player to guess 5 times
for guessesTaken in range(1,6):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Too low!')
    elif guess > secretNumber:
        print('Too high!')
    else:
        print("That's correct! The number is " + str(secretNumber) + ". You guessed it within " + str(guessesTaken) + " guesses!")
        break
