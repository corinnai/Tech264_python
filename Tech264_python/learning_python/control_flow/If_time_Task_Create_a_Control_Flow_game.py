#The options
    #Battle Game
    #Dice roll game
    #Interactive quiz game
# All the games should use the CLI (not anything like the pygame library).


#Battle game
    #Make a 2 player battle game using Python.
    #Player selects a character / fighter( from 4 - 6) or gets one assigned to them randomly. If Player 2, let them pick the character / fighter they want.If CPU, assign a character / fighter randomly.
    #The two Pokemon / fighters / characters need to fight.
    #A winner must be declared via some sort of calculation.
    #Bonus: Want to play again?

#Note: No Pygame or Turtle allowed.CLI only.

fighters = {
    "Warrior": {"attack": 8, "defense": 6},
    "Mage": {"attack": 10, "defense": 4},
    "Archer": {"attack": 7, "defense": 5},
    "Knight": {"attack": 6, "defense": 8},
    "Assassin": {"attack": 9, "defense": 3},
    "Paladin": {"attack": 5, "defense": 7}
}

print("Welcome to the Battle Game!")
