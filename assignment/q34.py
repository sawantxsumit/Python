#wap to print the pattern
'''
     *
    ***
   *****
  *******
'''

    
j=3
for i in range(1,5):
    print(" "*(j), end=" ")
    print("*"*(i*2-1))
    j=j-1

