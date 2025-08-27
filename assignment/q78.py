#Write a Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.

n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    sum+= 1/i
print(round(sum,3))