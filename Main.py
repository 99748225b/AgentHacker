





#Number Guesser
import random

password = random.randrange(0,100)
guess = 1
print(password)

while(True):
    print("Guess the password")
    userGuess = int(input())

    if userGuess > password:
        print("Too High")
        guess += 1
    elif userGuess < password:
        print("Too Low")
        guess += 1
    else:
        break
print(f"Correct! The number was {password}. You got it in {guess} guesses!")

