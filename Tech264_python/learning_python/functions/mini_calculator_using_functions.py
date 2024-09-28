from math_operation import *
# Create a Python file called calculator.py and complete a viable basic calculator using functions.

# MVP(each of these should be in a separate function):
#     Can add 2 numbers
#     Can subtract 2 numbers
#     Can multiply 2 numbers
#     Can divide 2 numbers

# Taking it to the next level:
#     Implement more complex operations, such as handling parentheses, exponentiation
#     More advanced operations should continue to be broken into separate functions



def calculator():
    num1 = float(input("enter a number : "))
    num2 = float(input("enter a number :"))
    operation = input("Choose operation(+, -, *, /): ")

    if operation == "+":
        print(add(num1, num2))

    elif operation == "-":
        print(subtract(num1, num2))

    elif operation == "*":
        print(multiply(num1, num2))

    elif operation == "/":
        print(divide(num1, num2))
    else:
        print("error")
calculator()