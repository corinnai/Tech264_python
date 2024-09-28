#Rationale
from idlelib.pyshell import use_subprocess

#Practice control flow
#Practice completing user stories

#Task
#Level 1
#Challenge yourself to get Level 1 done in 15 min
#Comments in the code are to help you meet user requirements, but you may need to write code in the order you think is necessary

# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
# Ask user for input
# Check if this input matches magic_number
# Let the user know if the response was correct or not
# Allow the user 5 guesses



#while number_to_guess:
   # user_try = int(input("guess the number:"))
    #if user_try == magic_number:
        #print(f"You guessed the right number which is {magic_number}")
        #number_to_guess = False
    #elif not user_try == magic_number and  attempts != 1 :
       # attempts -= 1
        #print(attempts)
   # else:
        #number_to_guess = False
        #print("You lost no more attempts ")

#Level 2
#Challenge yourself to get from Level 1 to Level 2 in 10 min
# User story 2
# As a user, I want to be able to guess a number and know if I need to go higher or lower.

# ask user for input
#check the input with the guessed one
#then if is right do smth
#if not check if 20 > guessed nr print u need to go higher if 20< guessed nr print u need to go lower

# User story 3
# As a user, I don't want my guesses wasted if I enter something accidentally as my guess which are not digits.

# User story 4
# As a user, after each guess, I would like to know how many guesses I have left.

#Level 3
#Challenge yourself to get from Level 2 to Level 3 in 10 min
# User story 5
# As a user, I would like the magic to be randomly generated each time I play so it is more fun.

# User story 6
# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.

#Hint: #Use the Python library random to generate a random number rather than assigning one




import random

magic_number = random.randint(1, 100)
number_to_guess = True
attempts = 6
#winning_number = 44

while number_to_guess:
    #print(magic_number)
    user_input = (input("guess the number between 1 and 100:"))

    if user_input.isdigit() :
        user_input = int(user_input)

        if user_input == magic_number :
            print(f"You guessed the right number which is {magic_number}")
            number_to_guess = False

        elif magic_number >= user_input and attempts !=1 :
            attempts -= 1
            print(f"you need to go higher and you have {attempts} attempts ")

        elif magic_number <= user_input and attempts !=1 :
            attempts -= 1
            print(f"you need to go lower and you have {attempts} attempts ")

        else:
            number_to_guess = False
            print(f"Sorry, you've used all your guesses. The magic number was {magic_number}.")

    else :
        print(f"Enter a digit ")








