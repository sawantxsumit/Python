#wap to find sum of even digits and products of odd digits of a given number

n= int(input("enter a number :")) 
sum=0
product=1
while(n>0):
    r=n%10
    if r%2==0:
      sum=sum+r
    else:
      product=product*r
        
    n=n//10
        

print("sum of even digits of the number is :",sum)
print("product of odd digits of the number is :",product)