n= int(input("enter a number "))

fact=1
if(n==0 or n==1):
    fact=1

else:
    for i in range(1,n+1):
        fact = fact*i
        
print("the factorial of " , n , "is ",fact)