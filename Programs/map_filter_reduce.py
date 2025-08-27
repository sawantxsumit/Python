# map
l=[1,2,3,4,5,6,7,8,9]

square=lambda x:x*x
sqlist=map(square , l)
print(list(sqlist))

# filter
def odd(n):
    if n%2==1:
        return True
    return False

onlyodd=filter(odd , l)
print(list(onlyodd))

# reduce
from functools import reduce

sum =lambda a,b:a+b

print(reduce(sum , l))

