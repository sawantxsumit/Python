
st= "hi My name is Sumit sawant "
p=open("file.txt" , "w")
d= p.write(st)
p.close()

p= open("file.txt")
data = p.read()
print(data)
p.close()

