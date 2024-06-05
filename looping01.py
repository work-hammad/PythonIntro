#LOops:
"""
Just like our daily life we need to do somethings repeatedly in programming for this we use loops. There are two types of loops in python:
1- For loop
2- While loop -----> There is no do while loop in python but we can make self-emulated do while loop i.e we can manually run loop for once and then check condition

"""

#range function is used very commonly for printing numbers upto 'n'
# syntax for range function is: range(start,stop,step)  ----> where start is inclusive and end is exclusive
#  for i in range(0,10,3):   we don't need to specify start as it will automatically be zero and step is also optional
for i in range(10):
    print(i, end=",")
print("\n")

ch='Hammad'
for character in ch:
    print(character)
print("\n")

list1=[7,8,9,0]
for j in list1:
    print(j)