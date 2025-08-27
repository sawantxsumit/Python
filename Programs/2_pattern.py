# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n)
#     else:
#         print("*", end="")    
#         print(" "*(n-2), end="")    
#         print("*", end="")  
#         print("")
         
n=int(input("enter a number :"))
# method 1
# k=10
# for i in range(1 , 11):
#     print(n ,"X", k , "=" , n*k )
#     k -= 1

# method 2
for i in range(1 , 11):
    print(n ,"X", 11-i , "=" , n*(11-i) )
    
    
          