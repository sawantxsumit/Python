'''
WAP to input amount and calaculate based on discount rate 
amount discount
0-5k     5%
5k-10k   12%
10k-20k  20%
20k-25k  30%
'''

a=int(input("enter sales amount :"))

if (a>0 and a<=5000):
    d=5/100*a
    print("discount =", d)
    print("amount to pay :", a-d)
elif(a>5000 and a<10000):
    d=12/100*a
    print("discount =", d)
    print("amount to pay :", a-d)
elif(a>10000 and a<=20000):
    d=20/100*a
    print("discount =", d)
    print("amount to pay :", a-d)
elif(a>20000 and a<=25000):
    d=30/100*a
    print("discount =", d)
    print("amount to pay :", a-d)
else:
    print("enter amount between 0-25000")