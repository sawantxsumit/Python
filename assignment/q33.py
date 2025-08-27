#wap to find factorial of a number

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     fact=1
#     for i in range(2,num+1):
#         fact=fact*i
#     return fact


num=int(input("enter a number :"))
fact=1
if num==0 or num==1:
        fact=1
else:
    for i in range(2,num+1):
        fact=fact*i
print("Factorial is :",fact)