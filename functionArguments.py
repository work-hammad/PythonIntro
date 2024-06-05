#Arguments:
"""
Function arguments are the values that are passed to the function for performing the designated task.
There are four types of arguments that are passed to the function:
1- Default Arguments
2- Keyword Arguments
3- Variable length Arguments
4- Required Arguments


"""
#Default Arguments: The values that are assigned to the parameters at the time of creation of function. Even if we don't pass any values
#during function call even then there will be no problem in executing the function but if we pass the values the default values will overriden

def average(a=5,b=3):
    print("Average is:",(a+b)/2)

average()
# average(7,9)
# average(12)
# average(b=7)

#keyword Arguments: These are specified pass values i.e we pass the values as key=value. For this we even don't need to worry about
#the order in which values are passed
def average(a=5,b=3):
    print("Average is:",(a+b)/2)

average(b=19, a=3)


#Required Arguments: These are the values that are passed normally withot key=value format for this correct order or sequence matters
def average(a=5,b=3):
    print("Average is:",(a+b)/2)

average(4,8)

#Variable length Arguments:Variable-length arguments in Python allow a function to accept a variable number of arguments. There are two cases: 
""" 1- Arbitrary arguments: When we want to accept any number of positional arguments to be passed to the function then we use * before the parameter. In this 
case values are passed to function as tuple"""

def sumAll(*num):
    sum=0
    for n in num:
        sum+=n
    
    return sum


x=sumAll(1,2,3,4,5,6,7,8,9,10)
print(x)

"""2- Keyword Arbitrary Arguments: When we want to accept any number of keyword arguments then we can use keyword arbitrary arguments list for this we need to 
use ** before the parameter. In this case values are passed to function as dictionary."""

def displayInfo(**var):
    for key,value in var.items():
        print(f"{key}:{value}")

displayInfo(name="Hammad", age=19, city="Multan")


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Hammad", lname = "Sarwar", fname = "Muhammad")


#we can also combine both of above cases to accept any number of positional or keyword arguments
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, a=3, b=4)

