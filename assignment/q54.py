# function 
# wap to add two values using a function

#with arguments 
# def sum(a,b):
#     return a+b

# a=int(input("Enter first number :"))
# b=int(input("Enter sceond number :"))
# print("sum of a and b is :", sum(a,b))

without arguments
# def sum():
#     a=int(input("Enter a :"))
#     b=int(input("Enter b :"))
#     c=a+b
#     print('sum of a and b is ', c)
# sum()

def smax(nums):
    nums.remove(max(nums))
    return max(nums)

nums=[2,3,4,5,6,7]
print(smax(nums))