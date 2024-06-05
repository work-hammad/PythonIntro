#String Formatting in python can be done with the help of format method 
sentence="My name is {} and I am {} years old"
#sentence="My name is {0} and I am {1} years old" ---> both ways are correct but not convenient
name="Hammad"
age=19
print(sentence.format(name,age)) 
#print(sentence.format(age,name)) ----> In the format method order is very important
""" A new method has been introduced by python after version 3.6 to format the string in a very convenient way that is fstring method"""


#fstrings:
"""
fstrings provide us a convenient way to embed valid python expression or variables inside string literals,  fstrings are perfixed with letter 
'f' and by placing curly braces {} inside the string literal and placing variables or expressions inside these curly braces.
These strings are evaluated at the runtime and the values of expression or variables are populated inside these curly braces.
"""
name="Hammad"
print(f"My name is {name}")
# print(f"My name is {{name}}")
print(f"{2**3}")


# Formatting numerical values with precision
pi = 3.141592653589793
formatted_pi = f"The value of pi is approximately {pi:.2f}"
print(formatted_pi)

# Performing arithmetic within an f-string
x = 5
y = 10
result = f"The sum of {x} and {y} is {x + y}"
print(result)
