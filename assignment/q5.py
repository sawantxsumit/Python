# wap to calculate total marks of 5 subject (full marks =100)
#as well as percentage of marks and division as per  the following conditions
''' 
>=80 -> grade A
>=60> grade B
>=40 -> grade C
<40 -> grade D
'''

a=int(input("Enter a number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
d=int(input("Enter fourth number :"))
e=int(input("Enter fifth number :"))

total= a+b+c+d+e
p= total/500*100

print("total obtained :",total)
print("percentage :", p)

if(p>=80):
    print("Grade A")
elif(p>=60):
    print("Grade B")
elif(p>=40):
    print("Grade C")
else:
    print("Grade D")
