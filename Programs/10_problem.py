from random import randint

class train:
    def __init__(self , trainNo):
        self.trainNo= trainNo
        
    def book(self , where , dest):
        print(f"the train number {self.trainNo} is booked from {where} to {dest} ")
    
    def getStatus(self):
        print(f"the train number {self.trainNo} is running on time")
    
    def getFare(self , where , dest):
        print(f"the fare for the train number {self.trainNo} from {where} to {dest} is {randint(200 , 4000)}")
        
p1= train(12790)

p1.book("bgp" , "delhi")
p1.getFare("bgp" , "delhi")
p1.getStatus()