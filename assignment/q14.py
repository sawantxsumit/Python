#WAP to print even numbers from 1 to n

n=int(input("enter a number :"))

for i in range(2,n+2,2):
    print(i)
    
sum=0
for i in range(2,n+1,2):
    sum+=i
print(sum)
    