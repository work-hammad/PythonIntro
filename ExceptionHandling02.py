#Finally Clause is used with exception handling for execution of the block of code which is guaranteed to execute
"""
Finally clause is used irrespective of the fact that exception is occured in try block or not or in simple terms whether we enter try or except
block the finally clause is always executed. As this always execution can also be done by removing the indentation after
the try except block so the question arises that what is the use of finally in exception handling? It is used in the cases when we wrap try 
and except in function and function returns certain value and still after returning the value we want some part of the code to be executed.
**Finally is generally used for clean up purposes i.e closing files, cleaning up resources and revoking purpose(i.e breaking the 
connection with database and thus freeing up resources)
"""


def func():
    try:
        nums=[1,2,4,3,5,6,7]
        x=int(input("Enter the index for which you want to access the list element: "))
        print(nums[x])
        return 1
    except IndexError as e:
        print(e)
        return 0
    finally:
        print("I am always executed")

x=func()
print(x)
    

"""
try:
    file = open("example.txt", "r")
    # Code for reading or processing the file
except FileNotFoundError:
    print("File not found.")
finally:
    # Close the file, even if an exception occurred
    file.close()
"""
