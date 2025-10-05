"""
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.
"""
# importing random library
import random

# Generate a random number 1-100 and store in a variable
generated_number = random.randint(1, 100)

# Loop True
while True:

    # This loop ensures that user enters a number between 1 and 100
    while True:
        # Take an input from the user
        user_input = input("Find the Lucky Number(1 to 100): ")

        try:
            guess = int(user_input)
            if 0 < guess <= 100:
                break
            else:
                print("Please enter a number between 1 and 100: ")

        # If ValueError occurs (It happens if user puts a string instead of number)
        # Program doesn't end but asks user to input a number again
        except ValueError:
            print("Invalid Entry! Please enter a number: ")

    # if else statements to find Lucky Number
    if guess > generated_number:
        print("No, the Lucky Number is lower")

    elif guess == generated_number:
        print("Congrats you found the Lucky Number!!!")
        break
    else:
        print("No, the Lucky Number is higher")
