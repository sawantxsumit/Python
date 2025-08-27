class Employee:
    language = "python"
    salary =120000
    
    
emp1= Employee()
emp1.name= "sumit"
print(emp1.name , emp1.salary , emp1.language)

emp2= Employee()
emp2.name= "abhishek"
emp2.age = 19
emp2.salary= 100000
print(emp2.name , emp2.salary , emp2.language ,emp2.age)
# here name is an object attribute also called instance attribute
# language and salary are class attributes

# instance attribute take priority over class attributes during assignment and retrieval