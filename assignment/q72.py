class sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a +self.b
 
a=int(input("Enter a number"))       
b=int(input("Enter second number"))       
s1=sum(a,b)
print(s1.add())