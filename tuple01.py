#Tuples:
"""
Tuples are ordered collection of data items. Tuple is similar data structure as list. The main difference between tuple and list is 
that tuples are immutable so they don't have methods like append or insert etc.
Syntax of tuples involve enclosing the elements in round brackets separated by commas.
For single elemnt tuple comma at the end is most to distinguish it with the int class element.
Indexing of tuple is same as list. We can access each element separately using indexing. Slicing a tuple return a new tuple and slicing 
is exactly same as of list and string i.e [start:stop:step]
Tuples also have the heterogenity property that is single tuple can have element of different data types.
"""

t=(1,2,5,7,9,2,6,3,4,10)
print(t)

details = ("Hammad", 19, "FR", 7.01)
print(details)

dt=(True,7,"Hammad",4.2,None)
print(dt)

stuple=(7,)
print(type(stuple),len(stuple))


