"""
String slicing is retrieving the required sequence of characters from string or it is the extraction of required portion of string
"""
#string[start:stop:step]
"""
Python automatically puts '0' at the start and length of string using len function at the end and step is optional
"""
#IMP: in string slicing [2:4] 4 will be omitted as syntax says it will slice the string and 2nd and 3rd character will get sliced
text = "Hello, World!"

# Extracting characters from index 0 to 5 (exclusive)
substring = text[0:5]
print(substring)  # Output: Hello -----> 5th character is omitted

# Using step to get every second character
every_second = text[0:12:2]
print(every_second)  # Output: Hlo o

# Omitting start and stop to get the whole string
whole_string = text[:]
print(whole_string)  # Output: Hello, World!

"""There are also lots of methods of string  that can be used to perform functions on strings"""
print(text.zfill)