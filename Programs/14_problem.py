import numpy as np


class vector:
    def __init__(self , x , y , z):
        self.x=x
        self.y=y
        self.z=z
        
    def __add__(self , v):
        return vector(self.x + v.x ,self.y + v.y  , self.z + v.z)
    
    def __mul__(self , p):
        return (self.x*p.x + self.y*p.y +self.z*p.z)
    
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
        
v1=vector(5, 6, 7)
v2=vector(12, 16, 17)

print(v1+v2)
print(v1*v2)