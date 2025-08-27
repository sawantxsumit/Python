class demo:
    a=9
    

one = demo()
print(one.a) 

one.a=10 #instance attribute is set
print(one.a)
#the instance attribute will not change the class atrribute although it takes priority over class attribute

print(demo.a)