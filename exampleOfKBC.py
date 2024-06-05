print("Hello and welcome to the show kon banega crore pati")
questions = [
    ["How many months have 28 days in them?",7, 9, 11, 12],
    ["What is the capital of Afghanistan?", "Islamabad", "Delhi", "Kabul", "Istanbul"],
    ["How many players are allowed in a squad of a cricket team?",12, 13, 14, 15],
    ["Who is the founder of Pakistan?","Quaid-e-Azam", "Allama Iqbal", "Sir Syed", "Liaquat Ali"]
]
money=0
levels=[1000,2000,4000,8000]
print("Answer the following questions from options 1-4 and press 0 to quit")

for i in range(len(questions)):
    q=questions[i][0]
    print(f"Questions for Rs{levels[i]}")
    print(q)
    print(f"1.{questions[i][1]}        2.{questions[i][2]}")
    print(f"3.{questions[i][3]}        4.{questions[i][4]}")
    reply=int(input("Enter the correct option: "))
    if reply==0:
        print(f"You have quitted the game .")
        break
    else:
        if i==0 and (reply==4) :
            print("Correct Answer")
        elif i==1 and (reply==3):
            print("Correct Answer") 
        elif i==2 and (reply==4):
            print("Correct Answer")
        elif i==3 and  (reply==1):
             print("Correct Answer")
        else:
            print("Incorrect Answer")
            break
                  
    money+=levels[i]
print(f"COngratulations. You are taking Rs {money} with you. ")

        




