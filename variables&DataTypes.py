#Variables:
"""
A varaiable is a named storage location for your data that is allocated on your computer's memory(ram)
Variables are just containers for storing your data we can modify the values inisde these containers and then retrieve them accordingly
Assignment operator is used to assign value to variables 
Variables can contain alphabets, numbers and underscores but there are some rules and conventions that need to be followed
while declaring variables
Python is a case sensitive langugage so small case and capital case letters are treated as two different enitities
We should give variables descriptive names so that we can understand what purose are they serving
usually camelcase convention is followed i.e more than word is joined using underscores to form a single variable
The scope of a variable refers to the region of the code where the variable can be accessed.
Variables declared inside a function have local scope, while variables declared outside any function have global scope.
"""

x=5.0        #float data type
count=0      #integer data type
flag=True    #boolean data type
result=None  #none type---->It is a special constant value that typically represents absence of value It is also default return type of functions that doesn't return anything
name="Hammad"#string type

print(x)
print(count)
print(flag)
print(result)
print(name)

#DataType:
"""
Actually data type is a classification to which type of value can be stored in variables. Understanding data types is fundamental 
in programming as it will determine which operation are supported by the respective data type and what are methods of handling such 
data type
Python is a dynamically typed language which means we don't need to explicitly define the data type the python interpreter infers it
on the basis of value stored in it but still it is very crucial to understand data types of variables to perform function correctly
In addition to above mentioned data types some other important data types supported by python programming language are 
list, tuple, set, dictionary, complexNumber, Bytes
"""


