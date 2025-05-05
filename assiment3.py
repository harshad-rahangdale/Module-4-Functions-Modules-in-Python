'''                            ASSIGNMENT 3:

                    Module 4: Functions & Modules in Python 
                   
                   Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
Expected Output:
For example, if the function is called with 5, it should return:
'''

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Sample number
num = 5
result = factorial(num)
print(f"Factorial of {num} is {result}")

''' 

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate mathematical values
sqrt_value = math.sqrt(num)
log_value = math.log(num)  # Natural logarithm (log base e)
sine_value = math.sin(num)  # Sine of the number (in radians)

# Display the results
print(f"Square root of {num}: {sqrt_value}")
print(f"Natural logarithm of {num}: {log_value}")
print(f"Sine of {num} (radians): {sine_value}") '''


import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate mathematical values
sqrt_value = math.sqrt(num)
log_value = math.log(num)  # Natural logarithm (log base e)
sine_value = math.sin(num)  # Sine of the number (in radians)

# Display the results
print(f"Square root of {num}: {sqrt_value}")
print(f"Natural logarithm of {num}: {log_value}")
print(f"Sine of {num} (radians): {sine_value}")