#List Comprehension:
"""
List comrehension is a concise way for creating lists from other iterables like some other lists, tuples, dictionaries, arrays
and even strings. 
Syntax: new_list=[expression for item in iterable if condition]
Actually they are use instead of for loops but they are preffered over traditional loops only when logic is one liner or short enough 
to maintain the readability of the program's logic

"""

sq=[i**2 for i in range(10)]
print(sq)

sq_pairs=[(i,i**2) for i in range(10)]
print(sq_pairs)


l=[x for x in range(10) if x%2!=0 ]
print(l)

nums=[1,2,3,4,5,6,7,8,9,10]
even_nums=[x for x in nums if x%2==0]
print(even_nums)

odd_nums=[x for x in nums if x%2!=0]
print(odd_nums)



names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)


#list methods
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
#m=l ----> doing this will alter 'l' as well when we print 'l' because m has also now become a reference to the already made list l
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m #-----> will concatenate both the list under the name of new list
print(k)
l.extend(m)#-----> will take m and paste it at the end of 'l' thus 'l' will be altered
print(l)
