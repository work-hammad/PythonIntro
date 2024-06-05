"""  
elif ladder is used when we have to make a decision based on more than one conditon 
it works in a way that whenever the condition is matched only that particular block is executed and then all other parts are ignored
and the part of code after elif block is executed and if no condition is matched then automatically else block gets executed 
"""

age=int(input("Enter your age: "))
vipPass=1

if age>18:
    print("You can drive")
elif age>=18 and vipPass==1:
    print("You can drive due to your VIP pass")
elif age<18:
    print("You cannot drive")
else:
    print("Input error")



