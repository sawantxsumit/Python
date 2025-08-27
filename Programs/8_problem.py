# program to check whether word "python" is present in a word file or not 
# also at which line 

with open("log.txt") as f:
    lines = f.readlines()
    
lineno =1

for line in lines:
    if("python" in line):
        print("python is present line no :" , lineno)
        break
    lineno+= 1
else:
    print("python is not present")
    
# here we are using for else commands
# else is executed only after for loop is executed 
# also when break is executed before the loop ends the else part is not executed
        
    
    