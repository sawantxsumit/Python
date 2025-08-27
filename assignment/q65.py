f=open('student.txt' , mode='r')
con=f.read()
for i in con:
    print(i,end="")
for i in f:
    print(i,end="")
f.close()