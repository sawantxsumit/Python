#wap to print this pattern 
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

for i in range(1,6):
    j=1
    for k in range(i):
        print(j, end=" ")
        j+=1
    print()