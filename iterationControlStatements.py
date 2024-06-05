#Control Flow Statements : Sometimes we want to modify loop's behaviour for this we use two statements break and continue

#Break Statement:
""" 
Break statement is used when at certain condition we want to exit the loop body
"""

character="Hamm7ad"
for ch in character:
    if ch=="7":
        break
    print(ch)


while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break    
  

  #Continue Statement:
  """
  It is used to skip the looping body for current iteration and move to the next iteration
  """

  for i in range(10):
     if i==5:
        continue
     print(i)



#printing a table using for loop and continue statement for only odd multiples
     
for j in range(12):
   if j%2==0:
      continue
   print("10 X ",j,"= ",10*j)
    
