#do while loop -----> There is no do while loop in Python but we can achieve the similar behaviour if we wantn
"""
The most common practice to make self emulated do while loop in python is to use an infinite while loop 
with a break statement wrapped inside an if statement
"""
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:  #It means that if number is not positive exit (break) the loop 
    break