#TypeCasting
"""
Typecasting or type conversion is the process of converting one data type to another data type
There are two types of typecasting: Explicit and Implicit typecasting
Explicit:
In Explicit typecasting user have to manually describe about the data type in which you want the result to be or it may be intermediate
process during any operation to make the data type same so that both objects are elligible for performing any operation on them

Implicit:
In implicit typecasting python automatically converts lower order data type to higher order data type during any operation
actually this is convention is made in order to prevent any data losses
i.e 
adding float with integer will result in float
"""
print(9+9.9)


a=5
b=5.5
number="10"
print(a+int(number))
print(b+float(number))
print(str(a), str(b))


