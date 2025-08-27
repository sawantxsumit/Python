#wap to find sum of digits of a given number
 


n= int(input("enter a number :")) 
sum=0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r

print("sum of digits of the number is :",sum)
    

    
    