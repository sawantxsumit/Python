s= {1, 2,3, 4} #set
t ={4, 6, 7,8,63}

e = set() #empty set
d={}  #empty dictionary

print(type(e))
print(type(d))

#set methods

e.add(99)
e.add(34)
e.add(957)
e.add(56)
print(e) 
print(s.union(t))
print(s.intersection(t))
print(s-t) 
print(t-s) 

#sets are unordered and unindexed
#cannot contain duplicate values

g= set()
g.add(20)
g.add("20")
g.add(20.0)
print(g)
# in python 20 == 20.0 because they are numerically equal 
# the different data type does not matter 
#hence the length if the set g will be 2




