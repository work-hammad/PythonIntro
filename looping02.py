""" 
While loops is used to repeatedly execute a block of code until a specified condition is true.
While loop require an incrementor i.e i=i+1 which will update the value after each iteration
"""

count=0
# count=5
while (count<5):
    print(count+1)
    count=count+1
    # count=count-1
#we can also execute a decrementing loop
else:
    print("I am inside else block")

    
"""----->We can also use else with while loop as condition of while loop becomes false we enter into the else block and 
even if at first condtion is false we directly enters into the else block without entering the while block"""


#we usually use while loops with complex conditions 
num=0
while(num<100):
    num=int(input("Enter a number: "))
    print(num)
print("Loop Exited")


