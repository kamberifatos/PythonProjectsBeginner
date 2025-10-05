# The program is modified so the user can specify how many dice they want to roll.
# and it counts the times the dice is rolled


# Here we import the random library to genereate a random number
import random

# defining variable
dice = []
counter = 0

# Initialize an infinite loop
while True:

    answer = input("Roll the dice? (y/n): ").lower()

    # checking if 'y' is typed
    if answer == "y":

        while True:
            user_input = input("How many dices do you want to roll?> ")

            # Handling the error if user doesn't type a number
            try:
                # converting user_input into an integer
                number_of_dices = int(user_input)
                if number_of_dices > 0:
                    break
                else:
                    print("Enter a positive number")
            # If ValueError occurs, this is printed and loop continues
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        print("(", end=" ")
        # for loop to write the values
        for number in range(number_of_dices):

            # genereating and puting the values in the dice list
            dice.append(random.randint(1, 6))
            print(dice[number], end=" ")

            # raising the counter by one (Just to keep check of dices rolled)
            counter += 1

        print(")")
        print("Number of rolls = ", counter)

    # checking if 'n' is typed
    elif answer == "n":
        print("Thanks for playing!")

        # breaking from the loop
        break

    else:
        # Continuing the input take unless y/n
        print("Invalid Entry!")
