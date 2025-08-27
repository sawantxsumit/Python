#method overriding

class A:
    def show(self):
        print('This is parent class')
        
class B (A):
    def show(self):
        super().show()
        print('This is child class')

obj1=B()
obj1.show()