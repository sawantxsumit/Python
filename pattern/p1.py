'''print pattern
   *
  ***
 *****
*******
'''

#right angle triangle
# for k in range(1,8,2):
#     print("*"*k)

#right angle triangle upside-down
# for k in range(7,0,-2):
#     print("*"*k)

#pyramid
# k=1
# for i in range(4,0,-1):
#     print(" "*(i), "*"*(k))
#     k=k+2
    
    
i=1
k=1
while(i<=5):
    while(k<=7):
        print("*"*k)
        k=k+1
    i=i+1
        
    