"""There are different methods with dictionaries that are qutite similar to that of list, sets, tuples, etc
Dicitonaries are widely used when we are working with databases i.e mongodB or pymongo"""

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1) 