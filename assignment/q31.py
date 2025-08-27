#wap to print this pattern 
'''
*
**
***
****
*****
'''

#using for loop
# j=4
# for i in range(1,6):
#     print("*"*i,end="")
#     print(" "*(j*2), end="")
#     print("*"*i)
#     j-=1

for i in range(1,6):
    print("*"*i)
    
#reverse of the above pattern
for i in range(4,0,-1):
    print("*"*i)
    
space=4
for i in range(1,6):
    print(" "*space, end="")
    print("*"*i)
    space-=1
#using while

# i=1
# while(i<6):
#     print("*"*i)
#     i+=1

