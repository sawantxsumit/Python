friend = ["sumit ", "yogesh " , "hariom" , 45 , 65 ,67.23 , False , 88]

print(friend)
friend.append("abhishek")
print(friend)
print(friend[1:6])
print(friend[0])

num =[1,2,3,43,1,3,4,5,32,3,3,23,4,77]
num.sort()
# num.reverse()
num.insert(3 , 5747)
value = num.pop(3)
num.remove(3)
print(value)
print(num)
print(43 in num) #returns true
print(max(num))
print(min(num))
list=[111 ,21 , 33]
a, b ,c = list
print(a,b,c)
print(sum(list))
print(num.count(1))

# list are mutable