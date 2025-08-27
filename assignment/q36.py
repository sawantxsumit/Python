#wap to print fibonacci series
#  0, 1, 1 , 2 ,3 ,5 ,8 ,13

# a=int(input("Enter the number of terms :"))
# s=1
# fib=0
# for i in range(a):
#     print(fib,end=" ")
#     fib+=s
#     temp=fib
#     fib=s
#     s=temp

#using recursion
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

term= int(input("Enter the number of terms :"))
for i in range(term):
    print(fibonacci(i))
    
    
    