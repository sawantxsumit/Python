# we can merge two dictionaries
dict1={1:"a" , 2:"b"}
dict2={3:"c" , 4:"d"}

merged= dict1|dict2
# print(merged)

# we can open multiple files using with syntax
with(
    open("file.txt") as f1,
    open("donkey.txt") as f2,   
):  
    content1=f1.read()
    content2=f2.read()

print(content1)
print(content2)
    

