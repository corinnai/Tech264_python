#Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

#The task
#Core:
#Make a new 'fizzbuzz.py' file
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz" instead of the number
#For numbers which are multiples of both three and five print "FizzBuzz"


number = 0


fizz_number = int(input("enter a fizz number :"))
buzz_number = int(input("enter a buzz number :"))

while number < 100:
    number += 1
    if number % fizz_number == 0 and number % buzz_number == 0:
        print("FizzBuzz")
    elif number % fizz_number == 0 :
     print("Fizz")
    elif number % buzz_number == 0:
        print("Buzz")
    else:
        print(number)

#If time:
#Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"
#Refactor using functions

