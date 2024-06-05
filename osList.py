import os
directory=os.getcwd()
os.chdir("/users")
print(os.getcwd)
folders=os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    # print(os.listdir(f"data/{folder}"))
    a=os.listdir(f"data/{folder}")
    print(a)