#wap to find prime factors of a number
# n=int(input("Enter a number :"))
# i=2
# while i<=n:
#     if n%i==0:
#         print(i , end=' ')
#         n=n//i
#     else:
#         i+=1
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

n=int(input("Enter a number :"))
print(fact(n))
        
        