"""
A program that simulates a game of Rock, Paper, Scissors.
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.
"""

# importing random library
import random

# creating a tulip(only-read list) for choices
choices = ('r', 'p', 's')

# creating a dictionary for letter to emoji replacement
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}

# While loop
while True:

    # Ask user to put r p s
    player_choice = input("Rock, Paper or Scissors? (r/p/s) --> ").lower()

    # When user types anything else then r / p /s
    if player_choice not in choices:
        print("Invalid Choice")

        # back to the start of the loop
        continue

    # Make computer choose one of 3 options
    computers_choice = random.choice(choices)

    # Display both options
    print(f"Player's choice  {emojis[player_choice]}")
    print(f"Computer's choice  {emojis[computers_choice]}")

    # If else statemnts to decide the outcome
    if player_choice == computers_choice:
        print("It's a draw!")
    elif (
        player_choice == 'r' and computers_choice == 's' or
        player_choice == 'p' and computers_choice == 'r' or
        player_choice == 's' and computers_choice == 'p'
    ):
        print("Player Wins!!!")
    else:
        print("Computer Wins!!!")

    # Ask if want to continue
    resume = input("Do you want to continue? (y/n) ").lower()

    # if not then break
    if resume != 'y':
        break
