#Match Case Statement:
"""
Match case is similar to switch case statement that is used in c language. Match case will compare given variable's value to different
shapes also reffered to as pattern. The goal is to compare and continue till the value is matched.
*Each has different body to be executed
*There is also default case which is executed when no case is matched i.e case_
*Its behaviour is similar as elif statement means whenever a case is matched the control is terminated out of the match case statement 
"""


num=int(input("Enter a number: "))
match num:
    case 1 | 2 | 3:
        print("Number is between 1 and 3")
    case 4 | 5 | 6:
        print("Number is between 4 and 6")
    case 7 | 8 | 9:
        print("Number is between 7 and 9")
    case _ if num==10:
        print("Number is 10")
    case _ if num==0:
        print("Number is zero")
    case _:
        print("Number is greater than 10")
    
       