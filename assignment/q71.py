# class car:
#     pass

# c1=car()
# c2=car()

# c1.window=4
# c1.tyres=4
# c1.engine='petrol'

# c2.window=6
# c2.tyres=8
# c2.engine='diesel'
# print(c1.engine)
# print(c2.engine)

#class program using constructor
class car:
    def __init__(self,window , tyres , engine):
        self.window=window
        self.tyres=tyres
        self.engine=engine

c1=car(4,4,'petrol')
c2=car(6,8,'diesel')

print(c1.engine)
print(c1.window)
print(c1.tyres)

print(c2.engine)
print(c2.window)
print(c2.tyres)
