#Lists:
"""
Lists are collection of ordered data items. It is one of the most widely used data structure that allows you to store 
and manipulate collection of data items. We can store items of different data types as well in a single list.
Its syntax involve the use of square brackets with elements separated by commas. Its index and slicing is same as of strings 
i.e index starts from zero and for slicing a list syntax is [start:stop:step]
"""
l=[3,4,2,6,9,7,0]
print(type(l))
print(len(l))

list1=[1,True,None,"Ali",7,"9"]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])

if "Ali" in list1:
    print("Yes")
else:
    print("No")

#Lists are mutable meaning we can alter and play with the content of lists
    
list1[0]=2
print(list1)

del list1[3]
print(list1)

print(min(l))
print(max(l))


print(l[1:7:2]) #positive indexing
print(l[-6::2]) #negative indexing