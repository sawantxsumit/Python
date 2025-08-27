#print a b c d pattern
ch=65
row_no=int(input("enter pattern length :"))
for row in range(1,row_no+1):
    for column in range(1,row+1):
        print(format(chr(ch)),end=" ")    
    ch=ch+1
    print()
    