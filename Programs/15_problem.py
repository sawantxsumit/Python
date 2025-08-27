n=int(input("enter a number :"))

table=[n*i for i in range(1,11)]

with open ("table_n.txt" , "a") as f:
        f.write(str(f"{table}\n"))
