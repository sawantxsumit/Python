class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x} + {self.y}i"
    
    #dunder methods
#     __init__: This method is called when you create an object of a class. It's used for initialization.
#    __str__: This method defines how an object is represented as a string when you use the print() function or convert it to a string.
#    __repr__: This method returns a string representation of an object that is suitable for debugging and evaluation.
#    __add__: This method is called when the + operator is used on two objects of your class.
#    __len__: This method is called when the len() function is used on an object of your class.


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1+p2)  # Output: (4, 6)