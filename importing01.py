#Import:
"""
In python import statement is used to bring external modules and packages in your program allowing you to use 
methods, classes, varaibles defined in these modules.
"""
#import math ----> importing an entire module
#from math import sqrt ----->importing a specific function from a module
#import math as m -----> importing a module with an alias (short name) that can be used in the program to avoid naming conflicts
#from math import * ----> this will import all the items from a module however it is not a recommended practice to do so
"""There is  a difference between import math and from math import * 
First practice improves readablitiy actually it brings the whole module to your program and you need to use module name and dot 
to access its methods and other functionalities
Whereas second practice brings all the items of module to your program and you don't need to use module name to access its methods and 
attributes so it is not preffered as it may cause confusions and conflicts with variable names and methods 
"""

import math as m
result=m.sqrt(6)
print(result)

#to see all the items of a module we can use dir function
import dateutil
print(dir(dateutil))

import datetime
print(dir(datetime))

#besides we can also use import statememt with condition if else to import a certain module when the condition is met
#this is useful when you want to bring the module at runtime fulfilment of certain condition