class employee:
    company = "wipro"
    def __init__(self):
        print("employee constructor")
    
        
class programmer(employee):
    company = "tata"
    def __init__(self):
        print("programmer constructor")
        
class coder(programmer): #this is an example of multilevel inheritance 
    company= "reliance"
    def __init__(self):
        super().__init__() 
        # super method is used to run the constructor of the parent class also
        print("coder constructor")
        

        
a=coder()