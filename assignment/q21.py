#wap to check whther a given number is palindrome or not

n= int(input("enter a number :")) 
x=n
rev=0
while(n>0):
    rev=rev+n%10
    rev=rev*10
    n=n//10
rev=rev//10

if rev==x:
    print("palindrome")
else:
    print("not a palindrome")
