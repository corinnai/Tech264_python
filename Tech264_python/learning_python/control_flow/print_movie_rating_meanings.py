#Task: Print movie rating meanings
#Objective
#Practice using one if statement that uses else if and else

#The task
#The if statement you make will below will print the meaning of the movie rating specified at the beginning of the code.
#You should only need to replace the lines in CAPITALS with your own code.

#Starting code:
# possible film ratings are "universal", "pg", "12", "12a", "15", "18"
film_rating = "12a"

# use an if statement to check for "universal" rating
# IF STATEMENT GOES HERE
if film_rating == "universal":
    print("all age groups can watch this film")

# check if film rating is "pg"
if film_rating == "pg":
    print(film_rating)
# ELSE IF STATEMENT GOES HERE
else:
    print("General viewing, but some scenes may be unsuitable for young children.")

# check if film rating is "12" or "12a"
if film_rating == "12" or "12a":
    print(film_rating)
# ELSE IF STATEMENT GOES HERE
else :
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# check if film rating is "15"
if film_rating == "15":
    print(film_rating)
# ELSE IF STATEMENT GOES HERE
else:
    print("No one younger than 15 may see a 15 film in a cinema.")

# check if film rating is "18"
if film_rating == "18":
    print(film_rating)
# ELSE IF STATEMENT GOES HERE
elif film_rating < "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
# ELSE STATEMENT GOES HERE
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")