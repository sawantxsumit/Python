# destructor

class Employee:
    def __init__(self):
        print("Constructor , Employee data created")
    def __del__(self):
        print("Destructor called , employee data deleted")
    
e1=Employee()
del e1