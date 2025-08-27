#wap to find sum of square of digit of a given number

n= int(input("enter a number :")) 
sum=0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r*r

print("sum of sqaures of digits of the number is :",sum)
    
