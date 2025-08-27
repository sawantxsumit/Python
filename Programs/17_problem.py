from functools import reduce
l=[i*i for i in range(1,10)]
p=[11,3,4,3,56,45,76,4,6,745,678,345,678,467,974,24]
great= lambda a,b: a if a>b else b

max=reduce(great,p)
print(max)