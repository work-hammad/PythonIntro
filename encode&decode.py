# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into 
# secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
import random
import string
option=int(input("Choose one option\n 1 For Encode \t 2 For Decode \t any other key to quit\n"))
message=input("Enter message to encode or decode: ")
ran1="".join(random.choice(string.ascii_letters)for _ in range(3)) 
ran2="".join(random.choice(string.ascii_letters)for _ in range(3)) 
if (option==1 or option==2):
    if option==1:
        new=[]
        words=message.split(" ")
        # print(words)
        
        for word in words:
            if len(word)>=3:
                word=ran1+word[1:]+word[0]+ran2
                # print(word,end="")
                new.append(word)
            else:
                word=word[::-1]
                # print(word,end="")
                new.append(word)
        print("".join(new))
    elif option==2:
        new=[]
        for word in message:
            if len(word)>=3:
                word=word[3:-3]
                word=word[-1]+word[:-1]
                new.append(word)
            else:
                word=word[::-1]
                new.append(word)
        print("".join(new))




    