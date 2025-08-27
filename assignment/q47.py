#wap to count even and odd in list
a=[]
x=int(input("enter list size :"))
even=odd=0
for i in range(x):
    v=int(input("Enter a number :"))
    a.append(v)
    if v%2==0:
        even+=1
    else:
        odd+=1
print("even numbers :", even)
print("odd numbers :", odd)