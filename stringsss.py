#Strings
"""
Anything that you enclose in single or double quotes is string.
Strings are essentially sequence or array of textual data or characters. Single or Double quotes are used accordingly single quotes are used
when we require double quotes inside the our string for example to quote some quotation.
For Multiline string we use triple double or single quotes as python reads one complete string till EOL is encountered.
"""

a="Hammad"
print(a)

st="""
this is a 
multiline
string
and """
print(st)

"""
As we know that string is an array of characters so each character is indexed at a certain position and we can access each of
single character separately.
"""
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print("Using For loop")
for character  in a :
     print(character)
