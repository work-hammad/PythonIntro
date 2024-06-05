import time

# current_time=time.localtime()
formatted_time=time.strftime("%H:%M:%S")
print("The time right now is: ",formatted_time)


hour=int(time.strftime("%H"))

if hour<12 and hour>0:
    print("Good Morning")
elif hour>12 and hour<4:
    print("Good Afternoon")
elif hour>4 and hour<7:
    print("Good Evening")
else:
    print("Good Night")


