# 2. Get name, age and DOB details from a user
  # Get the user's name, age and DOB.
name = input("enter your name: ")
age = input("enter your age: ")
dob = input("enter your date of birth (dd/mm/yyyy): ")
height = input("enter your height :")


user = [name, int(age), dob, float(height)]
  # print the user's name, age and DOB to the screen
print(f"Hi {name} you are {age}, {dob}")



# 3. Mix all the data about a user into a list
#Use your code from the "Task: Get name, age and DOB details from a user".
#Mix the name, age and DOB into one list user_details_list
user_details_list = [name, age, dob]

#Print the user's name, age and DOB from the list
print(user_details_list)

#Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
if type(age) == int :
    age = int(age)
print(f"{age}, {type(age)}")

int_user_age = int(user_age)
user_details_list.append(int_user_age)

#Ask the user for their height in cm and save it to the variable height
height = input("enter your height :")

#Save height as a float in the list, and print the height from the list.
user_details_list.append(float(height))
print(f"{user_details_list[3]} cm")