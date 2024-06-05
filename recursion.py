#Recursion:
"""
The type of construct in the programming in which a function calls itself is called recursion and these functions are called 
recursive functions. There are few important points to keep in mind while making recursive call to functions:
*Recursion makes some complex problems' solution very elegant and concise.
*Use of recursion must be done very carefully as memory consumption could be serious con while using recursion.
*Recursion must converges to a base condition to avoid infinite recursive calls.
*It mirrors the mathematical induction concept.

"""

def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)

print(Factorial(6))

#0,1,1,2,3,5,8,13,21,......
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
for i in range(10):
    print(Fibonacci(i),end=",")


    

    