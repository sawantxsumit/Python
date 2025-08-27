# tuple
a=()
x=int(input("Enter the tuple size :"))
a=list(a)
for i in range(x):
    v=int(input("Enter a value:"))
    a.append(v)
print(a)
print(len(a))
print(type(a))


#add a new element in tuple
val=int(input("Enter a new element:"))
l1=()
l1=list(a)
l1.append(val)
l1=tuple(l1)
print(l1)

#update element
val=int(input("Enter an element to update:"))
i=int(input("Enter the index:"))
l2=list(l1)
l2[i]=val
l2=tuple(l2)
print(l2)

#remove elements
val=int(input("Enter an element to remove:"))
l3=()
l3=list(l2)
l3.remove(val)
l3=tuple(l3)
print(l3)

# a=eval(input("Enter a number :"))