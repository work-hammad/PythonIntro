#Operators:
"""
Operators are special symbols and characters that are used to perform specific operations on variables and values.
They are the tools to manipulate with the data. 
There are different types of operators in python that is arithmetic, comparison, logical, assignment operators and more.
"""
#Arithmetic Operators:
"""+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division
%   # Modulus (remainder after division)
**  # Exponentiation
//  # Floor Division (division rounding down to the nearest integer)
"""
print(6+5)
print(6-5)
print(6*5)
print(6/5)
print(6//5)
print(6%5)
print(6**5)


#Comparison Operators:
"""
They are used to compare two values and return boolean result
==  # Equal to
!=  # Not equal to
<   # Less than
>   # Greater than
<=  # Less than or equal to
>=  # Greater than or equal to
They return Boolean type either true or false.
"""
x = 5
y = 10

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Less than
print(x < y)   # True

# Greater than
print(x > y)   # False

# Less than or equal to
print(x <= y)  # True

# Greater than or equal to
print(x >= y)  # False


 #Logical Operators:
"""
They combine multiple conditions and return boolean result
and  # Logical AND
or   # Logical OR
not  # Logical NOT
"""
a = True
b = False

# Logical AND
print(a and b)  # False

# Logical OR
print(a or b)   # True

# Logical NOT
print(not a)    # False


#Assignment Operators:
"""
Assignment operators are just used to assign values to variables
=    # Assignment
+=   # Add and assign
-=   # Subtract and assign
*=   # Multiply and assign
/=   # Divide and assign
%=   # Modulus and assign
**=  # Exponentiate and assign
//=  # Floor divide and assign
"""
x = 5

# Add and assign
x += 3  # Equivalent to x = x + 3

# Subtract and assign
x -= 2  # Equivalent to x = x - 2

# Multiply and assign
x *= 4  # Equivalent to x = x * 4

# Divide and assign
x /= 2  # Equivalent to x = x / 2

print(x)  # 10.0

#Bitwise Operators:
"""
They are used to perform bit level operation on integers
&    # Bitwise AND
|    # Bitwise OR
^    # Bitwise XOR
~    # Bitwise NOT
<<   # Left shift
>>   # Right shift
"""
a = 5
b = 3

# Bitwise AND
print(a & b)  # 1

# Bitwise OR
print(a | b)  # 7

# Bitwise XOR
print(a ^ b)  # 6

# Bitwise NOT
print(~a)     # -6

# Left shift
print(a << 1)  # 10

# Right shift
print(a >> 1)  # 2

#Membership Operators:
"""
Check if a value is a member of a sequence (e.g., a string, list, or tuple)
in    # True if value is found in the sequence
not in  # True if value is not found in the sequence
"""
my_list = [1, 2, 3, 4, 5]

# Membership - True if value is found in the sequence
print(3 in my_list)  # True

# Membership - True if value is not found in the sequence
print(6 not in my_list)  # True

#Identity operators:
"""
Compare the memory locations of two objects
is    # True if both variables point to the same object
is not  # True if both variables point to different objects
"""
x = [1, 2, 3]
y = [1, 2, 3]

# Identity - True if both variables point to the same object
print(x is y)   # False

# Identity - True if both variables point to different objects
print(x is not y)  # True
