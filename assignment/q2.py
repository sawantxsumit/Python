#wap to find maximum between three numbers

a=int(input("Enter a number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if(a>b and a>c):
    print(a ,"is greatest")
elif(b>a and b>c):
    print(b, "is greatest")
else:
    print(c, "is greatest")