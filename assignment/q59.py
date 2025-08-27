# # with argument with return
# def sum(a,b):
#     c=a+b
#     return c

# a=int(input("Enter a :"))
# b=int(input("Enter b :"))
# print('sum of a and b is :' , sum(a,b))
t = (1, 2, 3)
new_element = 4
t = t + (new_element,)
print(t)
# Output: (1, 2, 3, 4)
