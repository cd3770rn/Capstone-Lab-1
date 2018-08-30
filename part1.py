import random

def guessTheNumber():
    number = random.randint(0, 10)
    guess = input("Guess a number between 0 and 10: ")

    if int(guess) < number:
        print("Sorry! Too low!")

    elif int(guess) > number:
        print("Sorry! Too high!")

    else:
        print("You guessed right!")