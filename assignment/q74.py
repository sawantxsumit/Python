class A:
    
    def show(self):
        print('hello')

    def show(self , firstname=''):
            print('hello' , firstname)
            
    def show(self,  firstname='', lastname=''):
        print('hello' , firstname, lastname)
        
a1=A()
a1.show()
a1.show("sumit")
a1.show('sumit', 'sawant')