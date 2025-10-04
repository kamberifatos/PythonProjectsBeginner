# Here we import the random library to genereate a random number
import random

# Initialize an infinite loop
while True:

    answer = input("Roll the dice? (y/n)")

    # checking if 'y' is typed
    if answer.lower() == "y":

        # giving a random number to 2 variables
        random_one = random.randint(1, 6)
        random_two = random.randint(1, 6)

        # printing them
        print(f"({random_one}, {random_two})")

    # checking if 'n' is typed
    elif answer.lower() == "n":
        print("Thanks for playing!")

        # breaking from the loop
        break

    else:
        # Continuing the input take unless y/n
        print("Invalid Entry!")
