"""
Name: Valentin Esparza
Date: May 24, 2026
Description: This program asks the user to guess a random number
between 1 and 10, tells them if the guess is too high or too low,
tracks the number of attempts, and demonstrates both a while loop
and a for loop.
"""

import random

print("Student ID: valesp7141")

# Get user information
userName = input("Enter your name: ")
studentId = input("Enter your Student ID: ")

# Greet the user
print(f"\nHello, {userName}! Welcome to the guessing game.")

# Generate random number
correctNumber = random.randint(1, 10)

# Variables
userGuess = 0
guessCount = 0

# Guessing loop
while userGuess != correctNumber:
    userGuess = int(input("Enter a number between 1 and 10: "))
    guessCount += 1

    if userGuess > correctNumber:
        print("Your guess was too high.")
    elif userGuess < correctNumber:
        print("Your guess was too low.")
    else:
        print("You guessed correctly!")

# Display number of tries
print(f"It took you {guessCount} tries to guess correctly.\n")

# While loop example
print("Output from the while loop:")

counter = 0

while counter < 5:
    print(f"{correctNumber} incremented by {counter + 1} is {correctNumber + counter + 1}")
    counter += 1

# For loop example
print("\nOutput from the for loop:")

for counter in range(5):
    print(f"{correctNumber} incremented by {counter + 1} is {correctNumber + counter + 1}")
