# n=int(input("enter a number :"))

# for i in range(1,n+1):
#     print(" "* (n-i) , end="")
#     print("*"* (2*i-1) , end="")
#     print("")
# the print statement in python by default prints 
# a new line after execution 
# so we can write end="" to make sure new line is not printed


#here print("") is written because this statement will by 
#default print a new line so we dont need to write \n
    
# pattern 2

n=int(input("enter a number :"))
for i in range(1, n+1):
    print("*"*i)

for i in range(1,4):
    print