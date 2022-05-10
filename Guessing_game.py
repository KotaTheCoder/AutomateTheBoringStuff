#Guessing game
import random

secret_number = random.randint(0, 100)

guess = ""

while guess != secret_number:
    guess = input("Guess the number!\n")

    if int(guess) == secret_number:
        print("You win!")
        break
    elif int(guess) > int(secret_number):
        print("Number is too big")
    elif int(guess) < int(secret_number):
        print("Your pp is too small")

