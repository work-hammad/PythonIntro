"""We can also use else statement with loops it is used in the case when we want to perform some action only on if loop completes
its iteration without fulfilling the condition for break. We can use both for and while loops with else
*Important point here is this that if the break is met in the loop then following else is skipped


for variable in iterable:
    # Loop body
    if condition:
        # Some code that might break out of the loop
        break
else:
    # Code to be executed if the loop completes without encountering a break

    """

for i in []:
    print("Object found in the list")
else:
    print("Object not found in the list")



for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Control is in the else block")
#In the above case else block will be skipped we can say that else acts as a part of loop iteration that is executed only when
#all the iterations of loop run successfully without encountering a break statement