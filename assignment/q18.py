#wap to find sum of cubes of digits of a given number


n= int(input("enter a number :")) 
cube=0
while(n>0):
    r=n%10
    n=n//10
    cube=cube+r*r*r

print("sum of cubes of digits of the number is :",cube)
    
