#wap to print sum of square from 1 to n

n=int(input("enter a number "))
sum=0
i=1
while(i<=n):
    sum=sum+i*i
    i=i+1

# for i in range(1, n+1):
#     sum=sum+i*i

print("sum of squares is ", sum)
    

