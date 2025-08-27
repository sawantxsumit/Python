#Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

a = [1, 2, -3 , 11 ,4 , 6,7 ,9]
x= 10

n=0
for i in a:
    if (a[n] + i) == x:
        print(f"the sum of {i} and {i+1} is {x} ")
        break
    n+=1
else:
     print("not found")
        