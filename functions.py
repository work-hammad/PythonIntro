#Functions:
"""
Functions are the block of code use to perform specific task i.e function to perform sum, average, difference, etc.
*It is very much advisable to break your lengthy logic into chunks of code that are functions as it makes convenient for 
you to fix bugs and errors in your code
*Functions help in organizing and modularizing code, making it more readable, maintainable, and reusable.
*The main purpose of making funtions is to increase the reusability and readability.
*def keyword is used to define a function.
Also there are two types of functions: 
1- Built in functions 
2- User defined functions

There rules for naming functions are same as that for variables
Function help us to parallelize the work when working in a team
Indentation rules must also be followed while making functions

"""
import math
def sum(a,b):
    print("Sum of two numbers is ",a+b)

def gmean(a,b):
    print("The geometric mean of two numbers is ",math.sqrt(a*b))

def arithmeticMean(a,b):
    print("The arithmetic mean of two numbers is ",(a*b)/(a+b))

a=10
b=5
sum(a,b)
gmean(a,b)
arithmeticMean(a,b)


#In programming when we are making functions we can choose to define it later by following syntax

def isGreater(a,b):
    pass



    