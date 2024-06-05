#Comments are lines that describe or explain code to your future self or some other person who you are collaborating with 
#Comments are the part of your code that is not executed by your compiler because anything after the '#' is considered as redundant to compiler for execution
print("Above I have added comments(single line)")
print("There are two types of comments:\nsingle line and multi line")
'''
This is syntax for multi line comments as
you can see here
'''

"""
This is another way to add multi line comments
as I have use triple single quote first and then triple double quote
afterwards.
"""

#Important
'''
We Can also add comments by just first selecting the text and then pressing 
ctrl + / slash 
'''


#ESCAPE SEQUENCE CHARACTERS:
"""
Escape sequence characters are special characters within strings that may have a special function in syntax of the
coding language or they have special function associated to them in a way they may not be straightforward if you 
were to include them directly
"""

# print("FOr a new line
#       this is wrong syntax as 
#       it will cause an error")

print("The correct syntax to include a new line\n is this will \nautomatically start a new line in the console when you run the prog")
print("To add double quotes in your string you need to use \"double quotes\" in this way followed by a backslash")
print("Hello\rWorld")
# Output: Worldlo
print("Hello\tWorld")
# Output: Hello   World



#Parameters of print statement
#sep parameter:
"""
It is used to define the separator between different arguments in the print statement
It is an optional parameter to add
By default the separator parameter is set to space
Example is illustrated below:
"""
print("Muhammad","Hammad","Sarwar",7, sep="!")

#end parameter:
"""
It is a parameter used to define the end of a line in a print statement
It is also optional to add
By default the end parameter is set "\n" means a new line is added
Example is illustrated below:
"""

print("This is the execution of end parameter", end="\t")
print("After the addition of end parameter")


