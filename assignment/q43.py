a=[]
x=int(input("Enter list size :"))
for i in range(x):
    val=int(input("Enter the value :"))
    a.append(val)
print(a)
print(len(a))
a[0]='bca'
print(a)
#insert at last
v1=int(input("Enter a value to insert at last:"))
a.append(v1)
#insert
ind=int(input("enter the index :"))
v2=int(input("enter the value:"))
a.insert(ind,v2)
print(a)
#delete
v3=int(input("enter element which you want to delete :"))
del(v3)
print(a)
#pop
v4=int(input("enter the index which you want to delete :"))
a.pop(v4) #takes index as argument
print(a)
#clear
# a.clear()
# print(a)
#extend
a.extend([i for i in range(5)])
b=[33,33, 45, 12,44, 77]
a.extend(b)
print(a)
print(b)
#min
print(min(b))
#max
print(max(b))
#reverse
b.reverse()
print(b)
print('count the no of given element ', b.count(33))

a=[]
x=int(input("Enter list size :"))
for i in range(x):
    val=int(input("Enter the value :"))
    a.append(val)
print(a)
print(min(a))
print(max(a))
a.append(12)
print(a)
c=int(input("Enter the element :"))
print('frequency of element in the list', a.count(c))
ind=int(input("Enter the value:"))
print('value is present at index :', a.index(ind))
a.sort()
print(a)

