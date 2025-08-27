#wap to find product of digits of a given number

n= int(input("enter a number :")) 
product=1
# while(n>0):
#     r=n%10
#     if(r==0):
#         n=n//10
#     else:
#         n=(n//10);
#         product=product*r

while(n>0):
    r=n%10 
    n=(n//10)
    product=product*r
    

print("product of digits of the number is :",product)
    