def generatetable(n):
    table="" 
    # intialize table variable as a string because write mode takes only string as an argument
    for i in range(1 , 11):
        table += f"{n} x {i} = {n*i}\n" #writing the table in the string
    
    with open(f"table/tables_{n}.txt" , "w") as f:
        f.write(table) 
        # writing the table string to the table files and naming them using for loop
        # for this we must create a folder named table first
        
for i in range(2 , 21):
    generatetable(i)        