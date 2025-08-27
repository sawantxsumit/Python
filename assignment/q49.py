#wap to find sum of even digits and product of odd digits in a list
a=[]
x=int(input("enter list size :"))
even=0
odd=1
for i in range(x):
    v=int(input("Enter a number :"))
    a.append(v)
    if v%2==0:
        even+=v
    else:
        odd*=v
print("sum of even numbers :", even)
print("product of odd numbers :", odd)