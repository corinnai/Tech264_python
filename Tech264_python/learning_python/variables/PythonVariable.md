# Python Variable basics
   

## 1. Explain: What is a variable 
 `A variable is a symbolic name for a value. It allows you to store infromation that can be used and manipulated throught the program. `

## 2. Why called a variable? 
    `Is called a variable because the data it holds can vary or change during execution.`


## 4.Set/assign a variable 
### Try to set a variable with a number value 
### Try to set a variable with a decimal value 
### Try to set a variable with a string value 
    ```
        age = 25  # Integer value
        name = "Maria"  # String value
        height = 5.8  # Decimal value (float)
    ```
### How is using '==' different? 
    ` = is used to assign a value to a variable
      == is a comparison operator used to check if two values are equal`

## 5. Explain: What's the difference between a dynamically typed language (like Python) and a strong typed language 

*  Dynamically typed language (like Python):
    * 
          `The type of a variable is determined at runtime, and you don’t need to specify the type when declaring it.`
* Strongly typed language:
  *
        The type of a variable must be explicitly declared and cannot change once set. `
### Give an example of how they are different 
Python
  * ` variable = 42`

  *  `variable = " a string"` 

Java
  * ` int number = 42; `


## 6. Print the data types of the variables you set values for above 
    
    ` print(type(age))  # <class 'int'>
      print(type(height))  # <class 'float'>
      print(type(name))  # <class 'str'>`

## 7. Overwrite the value of one of your variables which stores a number 

    `age = 25
     print(age)  # Prints 25
     age = 30  # Overwriting the variable
     print(age)  # Prints 30`


### Check the id() of the variable before and after you overwrite the variable with a new number 
    ` age = 25
      print(id(age))  # Prints the memory address
      age = 30
      print(id(age))  

### Why does the 'id' of the variable change? 
    
    `In Python, when you overwrite a variable, it doesn't modify the existing object but creates a new object in memory with the new value. 
     The id() function shows the unique memory address where the object is stored. When you assign a new value, Python assigns a new memory address.`


## 8. Ask the user for some input and print the input to the screen 

    `user_input = input("Please enter something: ")
    print(" entered:", user_input)`


## 9. What is the difference between an operator and operand?

    `Operator: An operator is a symbol that performs a specific operation, eg +  `
    
    `Operand: An operand is the value or variable on which the operator performs the action, eg x , y`


## 10. Explain and demonstrate: Numeric data types: int and float
    * INT - integer represent whole number, without a deciamal point, either negative or positive , eg : 1, -1, 22
    
    * FLOAT - float represent real numbers , numbers with fractioanl part, have decimal point, eg : 0.5, -2.32


## 11. Explain and demonstrate: Boolean data type
    * BOOL - represents a value that is either True or False , is used commonly for comparisons, conditions and control flow
    ```
        x = 10
        y = 20
        result = (x > y)
        print(result)
    ```

## 12. Explain why the result is not 0.9999999... with this code and what lesson we should learn:
```

One_third = 1 / 3

 

print(One_third)

# Python should show 0.3333333333333333

print(One_third * 3)

# python rounds it to 1.0

```
*  computers represent numbers in binary(base-2), whereas humans usually work in decimal(base-10). 
  * when a number like 1/3 is expressed in decimal is an infinite repeating fraction :0.333
    * while humans can recognize this repeating pattern, computers store numbers using a finite number of bits, make it impossible to store the exact infinite fraction
      * unlike decimal(base-10), where we can represent some fractions like 0.5 as 1/2, binary (base-2) cannot represent certain fractions exactly 
        * in binary fraction is represented as a sum of powers of 1/2, 1/4, 1/8..
          * in some decimal fractions like 1/3 have no binary representation because they cannot be expressed as a sum of power of 1/2
            * For example : in decimal 1/3 is 0.3333...
                            in binary 1/3 is represented 0.01010101..
              * since the computers can only store a limited number of bits , they can only approximate this repeating sequence 
                *  The result is approximately 1.0 because Python applies a degree of rounding to make the output more human-friendly.





     * python uses floating-point arithmentic , which is based on binary representation
        the number 1/3 cannot be precisely represented as a float in binary
            when we multiply 0.333 by 3 the result is approximately 1 because of rounding and how floating-point numbers are stored in memory



Lesson to learn:
Floating-point precision issues:
Floats are not perfectly precise for many real numbers due to limitations in how computers represent them in binary. This can lead to small inaccuracies in calculations.
When dealing with calculations that require high precision (like financial calculations), it’s important to be aware of floating-point limitations. For exact arithmetic, consider using libraries like decimal in Python.

## 13. When does a string convert to False?
    
    A string converts to False when it is an empty string ("").
    
    string = ""
    print(f"string {bool(string)}")

## 14. When does a string convert to True?
        
    A string converts to True when it is non-empty (i.e., it contains one or more characters, including spaces, numbers, or any other characters).
    
    string = "hello"
    print(f"string {bool(string)}")

    string = " "
    print(f"string {bool(string)}")


## 15. What is None in Python?

    None - special constant that indicate that a variable or object doesnt have any value assignet to it

## 16. When is None commonly used?
        
    * Default return value for functions - return none by default if a function doenst explicitly reyurn a value
    * Missing or uninitialized Value -  When initializing a variable that will later hold a value, it can be set to None as a placeholder.
    * Optional Arguments: Functions can have default arguments set to None to indicate the absence of a value.
    * Sentinel Value: None can be used as a sentinel value to represent a condition that is distinct from any valid value.

## 17. Equivalent in Other Programming Languages:
    
    * JavaScript, Java , C#, C++ --- null
    * Ruby --- nil 

## 18. What happens when you convert None to a boolean?

    In Python, None is considered False in a boolean context.

## 19. Code to Assign x to be None and Check if it is None:
    
    x = None
    print(f"Boolean value of None: {bool(x)}")

## 20.
    
    hi = "Hello World!"

     Find out if 'hi' is made up of letters only (use one of the string methods)
            print(hi.isalpha())  # False, because the string contains spaces and punctuation

     Find out if 'hi' is made up only of lowercase letters (use one of the string methods)
            print(hi.islower())  # False, because the string contains uppercase letters and punctuation

    Find out if 'hi' is made up only of uppercase letters (use one of the string methods)
            print(hi.isupper())  # False, because the string contains lowercase letters and punctuation

    Find out if 'hi' ends with an exclamation mark (use one of the string methods)
            print(hi.endswith('!'))  # True, because the string ends with an exclamation mark

    Find out if 'hi' starts with a capital "h" (use one of the string methods)
            print(hi.startswith('H'))  # True, because the string starts with a capital 'H'
