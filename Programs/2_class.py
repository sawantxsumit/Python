class Employee:
    language = "python"
    salary =120000
    
    def __init__(self , name , salary , language):
        self.name =name
        self.salary =salary
        self.language =language
        print("this is a dunder method") 
# a dunder method is automatically called 
# it starts with __
        
    def getinfo(self):
        print("The salary is " , self.salary , "the language is " , self.language )
    
    @staticmethod
    def greet():
        print("good morning")
# static method means that the greet function is not using any class object or attributes so writing 'self' is not required


# self is not a keyword it can be replaced with other variable names 
    
emp1= Employee("sumit" , 1200000 , "cpp" )
# emp1.name= "sumit"
print(emp1.name)
emp1.getinfo()
# Employee.getinfo(emp1)