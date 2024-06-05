#OS module:
"""
It is a built in python package that allows you to interact with operating system. It allows you to perform various system related 
tasks such as file and dirctory manipulation, process management, etc
"""


import os 
if not os.path.exists("data"):
    os.mkdir("data")
for i in range(10):
    os.rename(f"data/new{i+1}",f"data/meow{i+1}")




   
    