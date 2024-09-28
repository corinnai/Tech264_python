# 1. Create strings and use quotes appropriately
# Why does this fail? -- syntax error , because the inner single quotes conflict with the quotes use to define the string
#1.
bad_string = "I said 'Wow!'"
print(bad_string)

#2.
bad_string = 'I said \'Wow!\''  # \ -- escaping a character
print(bad_string)

#3.
bad_string = 'I said "Wow!"'
print(bad_string)

#What is best practice when deciding what quotes to use around strings in Python?
'''
Consistency: Stick to either single or double quotes consistently in your code. Choose based on readability and ease of use, especially when embedding quotes inside the string.
'''




# 2. Slice strings --- Explain: What is slicing strings?
#       - can return a range of characters by using slice syntax
#       - specify the start index and the end index, separated by a colon, to return a part of the string
b = "Hello, World!"
print(b[2:5])


Hw = "Hello world!"
print(Hw)

# Find out how many characters Hw has
print(len(Hw))  # function to return the length of string

# Get the character in the first position in Hw
print(Hw[0])  # Index starts from 0, so Hw[0] - first character

# Get the last character
print(Hw[-1])  # Last character

# Get the 2nd last character
print(Hw[-2])


# Write a comment to EXPLAIN what does this do
print(Hw[2:])  #this slices the string starting from the 3th(index 2) character to the end


# Write a comment to EXPLAIN what does this do
print(Hw[-3:]) # This slices the string starting from the 3rd last character to the end


# Write a comment to EXPLAIN what does this do
print(Hw[:5])  # This slices the string from the beginning up to the 5th character (not including it)


# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[1:5])



















