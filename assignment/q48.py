#wap to find sum of numbers in a list
a=[]
x=int(input("enter list size :"))
sum=0
for i in range(x):
    v=int(input("Enter a number :"))
    a.append(v)
    sum+=v
    
print("sum of numbers in the list :", sum)