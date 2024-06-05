#ShorthandifElse Statement:
"""
Short hand if else statement is syntax for one liner if else condition that is short in logic to implement.
It is convenient only if the logic is short enough to implement in one line other wise the logic becomes messy if you try to implement large 
if else ladder in one line. This syntax is made for increasing the readability so it must be dealt with care while implementing.

"""
#result={value_if_condition_is_true} if condition {value_if_condtion_false} also there is a syntax to use it with print statement

a=10
b=12
print("a") if (a>b) else print("b") if (a<b) else print("none")
h=9 if a>b else 10
print(h)
