"""
In nested if else statements level of indentation decides where the control of progrm is.
"""

# number=10
number=int(input())
if number>0:
    if number<=10:
        print("Number is between 1 and 10")
    elif number>10 and number<=20:
        print("NUmber is between 10 and 20")
    else:
        print("Number is greater than 20")
elif number<0:
    print("Number is negative")
elif number==0:
    print("Number is zero")
else:
    print("Expression entered is not a valid number")


