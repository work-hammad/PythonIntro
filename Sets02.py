#Sets have many methods to manipulate and play with them accodingly
#union: means set of both elements but individual sets will still remain intact and overlapping elements will not repeat

# s1={"Hammad",7,"Akbar",True}
# s2={"Hammad",2.4,"Sajid",False,None}

# print(s1)
# print(s1.union(s2))
# print(s1,s2)

# # print(s1.update(s2))
# # print(s1,s2)
# iset=s1.intersection(s2)
# print(iset)

#Long story short update will update the specified set by performing the operation and simple union or intersection will keep sets unchanged

s1={1,2,2,3,4,5,5,6,7}
s2={4,4,5,5,7,8,9,6}
#symmetric diffference A union B - A intersection B
#while simple difference is excluding the common elements from the first set i.e A-B will return all uncommon elements that are only present in A
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

"""Similarly there are so many more methods of set with their associated functionalities i.e add,remove,discard,pop,clear"""
#del keyword can be used to completely delelte a set and if we furhter continue to access the same set a name error will be raised

