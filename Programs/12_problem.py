class employee:
    salary= 234
    increment =15
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increment= ((salary/self.salary)-1)*100
        
        
a=employee()
print(a.salaryAfterIncrement)
a.salaryAfterIncrement =500
print(a.increment)