import os

print(dir(os))
print(dir(os.path))
# from datetime import datetime
# x=os.getcwd()
# print(x)
# os.chdir(r"C:\Users\being\OneDrive\Desktop\New folder")
# print(os.getcwd())
# os.makedirs("Data/tut/new",exist_ok=True)
# os.chdir(r"C:\Users\being\OneDrive\Desktop")
# print(os.getcwd())
# current_directory=r"D:\10 Days Python Code\Day5"
# os.chdir(current_directory)
# print(os.getcwd())
# print(os.listdir())

# os.rename("enumeratee.py","ENUMERATEE.py")
# print(os.listdir())
# print(os.stat("ENUMERATEE.py"))
# print(os.stat("ENUMERATEE.py").st_size)
# mod_time=os.stat("ENUMERATEE.py").st_mtime  #----> gives the last modified time and date
# print(datetime.fromtimestamp(mod_time))  #----->gives date and time in human readable format



# print(os.getcwd())
# os.chdir(r"C:\Users\being\OneDrive\Desktop")
# print(os.getcwd())
# #os.walk() function generates the file names in a directory tree by walking either top-down or bottom-up through the directory tree
# for dirpath,dirnames,filename in os.walk(r"C:\Users\being\OneDrive\Desktop"):
#     print(f"Directory's path: {dirpath}" )
#     print(f"Directory's name: {dirnames}")
#     print(f"Files's name: {filename}")
#     print()

# print(os.environ.get("HOMEPATH"))
# for key,value in os.environ.items():
#     print(f"{key}:{value}")

# os.environ['MY_VARIABLE'] = 'my_value'
# for key,value in os.environ.items():
#     print(f"{key}:{value}")

# if 'MY_VARIABLE' in os.environ:
#     del os.environ['MY_VARIABLE']
# for key,value in os.environ.items():
#     print(f"{key}:{value}")


# file_path=os.path.join(os.environ.get("HOMEPATH"),"test.txt")
# file_path=os.path.join("C:\\Users\\being","test")
# print(file_path)
# print(os.path.exists(file_path))
# os.makedirs(file_path,exist_ok=True)

# print(os.path.isfile(file_path))
# print(os.path.isdir(file_path))



# path = '/path/to/somefile.txt'
# directory, filename = os.path.split(path)
# print(f"Directory: {directory}")
# print(f"Filename: {filename}")



# path = '/path/to/somefile.txt'
# root, extension = os.path.splitext(path)
# print(f"Root: {root}")
# print(f"Extension: {extension}")



# path = '/path/to/somefile.txt'
# path_components = path.split(os.sep)
# print(f"Path Components: {path_components}")



