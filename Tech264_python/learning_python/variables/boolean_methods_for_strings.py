# Find out  what is needed using the comments as a guide.Each of the methods used below should return a boolean(True or False only).
# You are not allowed to use any 'if' statements.


hi = "Hello World!"

# # find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
is_alpha = hi.isalpha()
print(is_alpha)

# # find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the screen
is_lower = hi.islower()
print(is_lower)

# # find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the screen

is_upper = hi.isupper()
print(is_upper)

# # find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen
ends_with_exclamation = hi.endswith('!')
print(ends_with_exclamation)

# # find out if 'hi' starts with a capital "h" (use one of the strings methods) - print the boolean to the screen

starts_with_h = hi.startswith('H')
print(starts_with_h)