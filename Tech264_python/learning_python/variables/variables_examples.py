#4. Set/assign a variable:

age = 25  # Integer value
name = "Maria"  # String value
height = 5.8  # Decimal value (float)

print(type(age))
print(type(height))
print(type(name))


age = 25
print(age)
age = 30
print(age)


age = 25
print(id(age))
age = 30
print(id(age))


user_input = input("Please enter something: ")
print("You entered:", user_input)



string = ""
print(f"string {bool(string)}")

string = "hello"
print(f"string {bool(string)}")

x = None
print(f"Boolean value of None: {bool(x)}")

hi = "Hello World!"
print(hi.islower())


x = 5
y = 1
#add
print(x + y)
#subtract
print(x - y)
#multiply
print(x * y)
#divide
print(x / y)
#find the remainder part of the division
print(x % y)

#greater than
print(x > y)
#less than
print(x < y)
#check if equal
print(x == y)
#check if not equal
print(x != y)
#greater than or equal to
print(x >= y)
#less than or equal to
print(x <= y)

