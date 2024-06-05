#DocStrings:
"""
Doc strings are the string literal that are written just after the function name or above the function body,module,
class or method.Their syntax is similar to that of comments but they are written at specific positions as mentioned earlier.
Comments are completely ignored by python interpreter but we can print the doc string using a specific method.
"""

def sum(a,b):
    """sum function takes two numbers as input and they
    print their sum as output"""
    print("The sum of two numbers is:",a+b)
sum(9,8)
print(sum.__doc__)

#PEP 8 or Python Enhancement Proposal is document or guide for writing python by providing conventions for writing clear, concise 
#readable and maintainable pyhton code. It is written in 2001 by guido van rossum,Barry Warsaw and Nick COghlan.
    