#wap to find the middle number in group of three numbers

a=int(input("Enter a number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if((a>b and a<c) or (a>c and a<b)):
    print(a," is the middle number")
elif((b<c and b>a) or (b<a and b>c)):
    print(b ,"is the middle number ")
else:
    print(c,"is the middle number")