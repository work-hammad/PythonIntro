#Sets:
"""
Set is a well defined collection of objects.Sometimes we want to 
make a list but we don't want duplication in our list as under some given conditions. Here are some important points:
*Set is unordered collection of data items
*Sets conntains data elements separated by commas enclosed within curly braces
*Items of set in python are unchangeable once you created them
*Creating empty set follows a special syntax to avoid repulsion with the syntax of dictionary
*Sets donot contain duplicate items
*Sets donot gurantee the order except for the case that set contains only int type
"""


s={6.0,8.1,2.2,9.9,3.4,1.9,5.6,5.8,9.1,0.6,4.4,7.6}
print(s)

s1={5,5,5,5,2,2,2,1,2,5,4,4,5,5,6,7,5}
print(type(s1))
print(s1)
#s1[0]=23-----> will generate an error
#s2={} -----> will be treated as dictionary
s2=set()
print(type(s2))


s3={"ant","fan","Chicharito","Dhaka"}
print(s3)
info = {"Carla", 19, False, 5.9, 19}
print(info)


for i in info:
    print(i)