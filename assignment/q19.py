#wap to check whether a given number is armstrong or not

# An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of 3. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 

n=int(input("Enter a number :"))
cube=0
x=n
l=len(str(n))
# while(n>0):
#     r=n%10
#     n=n//10
#     cube=cube+r*r*r
for i in range(l):
    r=n%10
    cube=cube+r*r*r
    n=n//10
    
if(cube==x):
    print("Armstrong number ")
else:
    print("not an armstrong number ")
