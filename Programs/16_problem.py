n=5
l=[str(i*n) for i in range(1,11)]
#we need to convert list into string because join function works only for strings


# with open("table_n.txt" , "a") as f:
#     for item in l:
#         f.write(f"{str(item)}\n") 
           
# with open("table_n.txt") as f:
#     content=f.read()
# print(content)

table="\n".join(l)
print(table)
