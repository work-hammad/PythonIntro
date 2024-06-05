# marks=[45,67,87,38,99,55]
# index=0
# for m in marks:
#     print(m)
#     if index==4:
#         print("Great Job man")      
#     index+=1
# print("Loop ended")

#Enumerate:
"""
Python has a built in enumerate function that allows you to iterate over a sequence i.e tuple,list,dictionary,etc while keeping the track
of index automatically whereas just using loop only we need to manually keep track of index.
*Enumerate function returns you tuple containing index and other object which is being iterated over and then we can use loop to
unpack this tuple and the value of index is incremented automatically by enumerate with each iteration.
Syntx: enumerate(iterable, start=0)
by default start value is zero and we can set according to our need.
"""

marks=[12,15,19,21,27,30,20]
for index,m in enumerate(marks):
    print(m)
    if index==5:
        print("You have got full marks")
print("Loop ended")


marks=[12,15,19,21,27,30,20]
for index,m in enumerate(marks,1):
    print(index,m)
    if index==5:
        print("You have got full marks")
print("Loop ended")
