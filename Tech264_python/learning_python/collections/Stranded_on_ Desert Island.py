# 4.  Finish the "Stranded on a Desert Island" game
# How are tuples similar to lists?
        # index and slicing
        # contain multiple data type
        # iteration
        # length
        # contain duplicates
    #Difference
        # Tuples are immutable

# Are tuples immutable and what does this mean?
    # means that once a tuples is created , its elements cant be modified
new_list = [1,2,3]
new_list[0]= 10
print(new_list)

new_tuple = (1,2,3)
#new_tuple[0] = 10

# What other data types are immutable?
    #strings
    #numbers
    #tuples
    #frozen sets
    #booleans

# What is a good use case for tuples?
    #Fixed data: When you have a collection of data that should not change.
        # For example, geographic coordinates (latitude, longitude) can be stored as tuples because these values should not change during runtime.
    #Dictionary keys: Tuples can be used as keys in dictionaries because they are immutable, while lists cannot be used.




# What does the following piece of code do?
essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

#Objective
    # Practice using tuples.
#The task
    # Add your code where it says 'YOUR CODE GOES HERE'

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code

print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

# save the items as a tuple
essentials_tuple = (essential_item2, essential_item2, essential_item3)

# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

# try to add the 4th item to the tuple
essentials_tuple = essentials_tuple + (essential_item4,)
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)
