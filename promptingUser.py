#Prompting user means asking an input value from the user for this purpose we use input() 
#in input function we give a string to prompt user
a=input("Enter your name: ")
print("Your name is ",a)

#The most important thing of input function is that it returns value of string so we must use typecast
#to convert it into the desired type required for the operation being performed 



x=input("Enter first number")

y=input("Enter second number")

print(x+y)                                                                                                          
# print(x-y)                                                                                                          
# print(x*y)                                                                                                          
# print(x/y)    ---> will not work as input is taken as string                                                                                                      
# print(x//y)   

print(int(x)+int(y))                                                                                                          
print(int(x)-int(y))                                                                                                          
print(int(x)*int(y))                                                                                                          
print(int(x)/int(y))                                                                                                          
print(int(x)%int(y))                                                                                                          
                                                                                       