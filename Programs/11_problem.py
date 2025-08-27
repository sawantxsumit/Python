class twoDvector:
    def __init__(self , x , y):
        self.x=x
        self.y=y
    
    def show(self):
         print(f"the vector is {self.x}i + {self.y}j") 
        
class threeDvector(twoDvector):
    def __init__(self, x, y , z):
        super().__init__(x, y)
        self.z=z


    def show(self):
         print(f"the vector is {self.x}i + {self.y}j + {self.z}z")   
         
         
p1= twoDvector(12 , 14)
p2= threeDvector(12 , 11 , 16)

p1.show()    
p2.show()    
        