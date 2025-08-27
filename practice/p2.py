from termcolor import colored

a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
print(a+b)
print(colored(f"the sum of {a} and {b} is {a+b}"), "green")
print(f"the product of {a} and {b} is {a*b}")
print(f"the difference of {b} and {a} is {b-a}")
print("division", b/a)
print("exponent ", a**b)
print("floor value", 67//10)
print("modulus", 87%10)

#Assignment operator
a+=3
print(a)
a-=1
print(a)
a*=2
print(a)
a/=2
print(a)
a**=2
print(a)

#relational operator
if(a==3):
    print("a==3")
if(a>b):
    print("a>b")
if(a<b):
    print("true a<b")
if(a>=b):
    print("true a>=b")

if(a<=b):
    print("true a<=b")

