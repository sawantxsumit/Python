class employee:
    company = "wipro"
    name = "sumit"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")
        
class programmer(employee):
    company = "tata"
    languauge="cpp"
    def showLang(self):
        print(f"the name of the employee is {self.name} and the language is {self.languauge}")
        
        
a=programmer()

a.showLang()
a.show()        