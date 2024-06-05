#Exception Handling:
"""
Exception is the error that occurs at runtime.
Exception Handling is the process of handling unwanted events that can occur in your program. Exception handling is actually 
way of dealing with errors in a controlled manner. Exception handling deals with these events to avoid the program to hault or crash
or crash because these errors will disrupt the normal operation of programs.
Python has many builtin exceptions that are raised when a specific type of error is occured. When an exception occurs python interpreter stops
the current process and passes the control to the calling process to handle the exception and if not handled program will crash

Syntax:
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the specific exception (ZeroDivisionError in this case)
    print("Cannot divide by zero!")
else:
    # Code to execute if no exception is raised
    print("Division successful!")
finally:
    # Code that will be executed no matter what (optional)
    print("This will always be executed.")



There are several types of errors that can occur in Python:

*Syntax errors: These occur when the code is not written in a proper format, and the interpreter is unable to understand it. For example, if you forget to close a parentheses or forget to indent code properly, you will get a syntax error.
*Name errors: These occur when you try to use a variable that has not been defined.
*Type errors: These occur when you try to perform an operation on a value of the wrong type. For example, if you try to add a string and a number, you will get a type error.
*Index errors: These occur when you try to access an element in a list or a string using an index that is out of bounds.
*Value errors: These occur when a built-in function receives an argument of the right type, but an inappropriate value.
*Attribute errors: These occur when you try to access an attribute of an object that does not exist.
*Import errors: These occur when you try to import a module that does not exist or cannot be found.
*Key errors: These occur when you try to access a dictionary with a key that does not exist.
*File not found errors: These occur when you try to open a file that does not exist or cannot be found.
*Indentation errors: These occur when the indentation of the code is not consistent, which can cause the interpreter to behave unexpectedly.
*Zero division errors: These occur when you try to divide a number by zero, which is not allowed in Python.
*Recursion errors: These occur when a function calls itself recursively, but the base case is not defined, causing the function to call itself indefinitely.
*Memory errors: These occur when the program tries to use more memory than the computer has available.
*Overflow errors: These occur when a calculation produces a result that is too large to be stored in the allocated memory.
*Underflow errors: These occur when a calculation produces a result that is too small to be represented accurately in the allocated memory.
*Assertion errors: These occur when an assert statement fails.
*Not implemented errors: These occur when a method or function has not been implemented yet.
*Runtime errors: These occur while the program is running and can be caused by a variety of factors, such as invalid input, missing resources, or other unforeseen circumstances.
*Security errors: These occur when the program tries to perform an action that is not allowed due to security restrictions.
*Timeout errors: These occur when a program takes too long to run and exceeds the allotted time limit.
*Unbound local errors: These occur when you try to access a local variable before it has been defined.
*Internal errors: These occur when the interpreter encounters an unexpected condition that it cannot handle.
*External errors: These occur when the program interacts with an external resource (such as a database or a network connection) and something goes wrong.

It is also worth noting that Python allows you to define your own custom errors using the Exception class. This can be useful if you want to create specific error handling logic for your program
"""


a=input("Enter the integer for which you want the table: ")
l1=[1,2]
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    # l1.insert(5,a)
    print(l1[int(a)])
    
except ValueError as e:
    print("Invalid input:",e)

except IndexError as e:
    print(e)
print("Some important lines of code")


        

