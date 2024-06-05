#Dictionaries:
"""
Dictionaries are ordered collection of data items(after version of python 3.7).
Dictionaries are actually mapping of keys to their corresponding values. They are called associated arrays or hash maps in other languages.

"""
dict1={"name":"M Hammad Sarwar", "age":19, "human being":True}
print(dict1)

#accessing elements inside the dictionary----> two ways first one will raise an error when the specified key is not present in the dictionary
print(dict1["name"])
# print(dict1["names"])
print(dict1["age"])
print(dict1["human being"])

print(dict1.get("name"))
# print(dict1.get("names")) ----->will return none

# print(dict1.keys())
# print(dict1.values()) 

#there is also another way to get the values corresponding to the keys from dicitonaries i.e
for i in dict1.keys():
    # print(dict1[i]) 
    print(f"{i}={dict1[i]}")

#another way to access key value pairs from dictionary is 
"""The .items() method is commonly used when you need to iterate over both keys and values 
or when you want to convert a dictionary to a list of tuples.
It's worth noting that the view object returned by .items() reflects changes made to the dictionary in real-time.
If the dictionary is modified, the view object will automatically reflect those changes.
 """
print(dict1.items())

for key,value in dict1.items():
    print(f"{key}:{value}") 
#this method is useful when you want to iterate over both keys and values simultaneously 


