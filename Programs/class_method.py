class demo:
    a=23
    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        

    
p=demo()
p.a=11 
#this will not change the value of a because we have already set show func as a classmethod
p.show()

p.name ="sumit sawant"
print(p.name)