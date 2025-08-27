'''
wap to print pyramid pattern
'''

a=int(input("Enter pyramid height :"))
# using for loop
# space=0
# for i in range(a,0,-1):
#     print(" "*(space), end=" ")
#     print("*"*(i*2-1))
#     space=space+1
    
# space=a
# for i in range(1,a+1):
#     print(" "*(space), end=" ")
#     print("*"*(i*2-1))
#     space=space-1
    
#using while loop
space=0
i=a-1
while space<=a and i>0:
    print(" "*(space), end=" ")
    print("*"*(i*2-1))
    space+=1
    i-=1

# space=a-3
# i=2
# while space>=0 and i<a:
#     print(" "*(space), end=" ")
#     print("*"*(i*2-1))
#     space-=1
#     i+=1
