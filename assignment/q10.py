#wap to print sum of cube from 1 to n

n=int(input("enter a number :"))
sum=0
for i in range (1,n+1):
    sum=sum+i*i*i
    
print("sum of cubes :", sum)