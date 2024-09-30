# Dice game
# Make a dice game:

#Let's make a game that rolls a dice and picks a winner.
#Start the game with a welcome message and ask if the user is ready to play.
#Get the user 's name and start a loop (While loop recommended)
#Use the random library and a method from that library to roll, a number 1 - 6
#Store the number in a variable
#Do the same for the computer
#Compare the two numbers, whose was bigger? Tell the user! and end the game
#Now add functionality to the game.Let the
#User and the CPU roll until one gets to 30.
#The one that gets there first is the winner!

#Bonus: Want to play again?

import random

# Welcome message
print("Welcome to the Dice Game!")

while True:
    # Asking if the user is ready to play
    ready = input("Are you ready to play? (yes/no): ").lower()
    if ready != 'yes':
        print("Maybe next time!")
        break

    # Getting the user's name
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}, let's start the game!")

    # Initializing scores
    user_score = 0
    computer_score = 0

    # Game loop
    while user_score < 30 and computer_score < 30:
        input("Press Enter to roll the dice...")

        # Rolling dice for user and computer
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)

        print(f"{user_name} rolled a {user_roll}")
        print(f"Computer rolled a {computer_roll}")

        # Adding rolls to scores
        user_score += user_roll
        computer_score += computer_roll

        print(f"{user_name}'s score: {user_score}")
        print(f"Computer's score: {computer_score}")

        # Check if there's a winner
        if user_score >= 30:
            print(f"Congratulations {user_name}, you won!")
            break
        elif computer_score >= 30:
            print("Computer wins this time!")
            break

    # Asking if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break
