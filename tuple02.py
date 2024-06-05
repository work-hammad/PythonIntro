#Tuples are immutable mean we cannot change tuples.
"""
For tuple methods we first need to convert a tuple into a list and then apply all the methods of the list
Still there are some tupple methods that donot alter the tuple so they are used accordingly
"""

t=("Hammad","Ali","Akbar","Zaid","Farhan")
temp=list(t)
temp.append("Gul")
temp.pop(2)
temp[1]="Bilal"
temp.insert(3,"Jahanzaib")
t=tuple(temp)
print(t)


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)----> valueError
# res = tuple1.index(3, 4, 8)---->will first slice from 4:8 and then give the index of first occurence of 3 in the sliced tuple
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)