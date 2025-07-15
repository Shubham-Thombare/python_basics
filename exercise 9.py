# Number Guesssing Game  (random numbers)

import random

low = 1
high = 50
answer = random.randint(low, high)
guesses = 0 

print("Python Number Guessing Game")
print(f"Select  a number netween {low} and {high}")

while True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low or guess > high:
            print("That number is out of range")
            print(f"Select  a number netween {low} and {high}")
        elif guess < answer:
            print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
        print()
    else:
        print("Invalid guess")
        print(f"Select  a number netween {low} and {high}")
        