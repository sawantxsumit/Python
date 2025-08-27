# p= open("file.txt")
# data = p.read()
# print(data)
# p.close()


# this can also be written as
with open("test.txt") as f:
    print(f.read())
    
# in this method we dont have to close the file explicitly