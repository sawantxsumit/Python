# try:
#     a=int(input("Enter a number :"))
#     print(a)
# except Exception as e:
#     print(e, "\nEnter an integer please")

# a=int(input("enter a number :"))
# b=int(input("enter second number :"))

# if(b==0):
#     raise ZeroDivisionError("you cannot divide a number by 0 ")
# else:
#     print(f"the division of a/b is {a/b}")

try:
    a=int(input("Enter a number :"))
    print(a)
except Exception as e:
    print(e, "\nEnter an integer please")

else:
    print("we are inside else block")

# else part executes when try is successful 