#wap to show assignment operators , relational operators and identity operators in python

a=int(input("enter the value of a "))
b=int(input("enter the value of b "))

#Assignment operator
a+=3
print(a)
a-=1
print(a)
a*=2
print(a)
a/=2
print(a)
a**=2
print(a)

#relational operator
if(a==3):
    print("a==3")
if(a>b):
    print("a>b")
if(a<b):
    print("true a<b")
if(a>=b):
    print("true a>=b")

if(a<=b):
    print("true a<=b")
    

#identity operators

if (type(a) is int ):
    print("integer")
else:
    print("not an integer ")





