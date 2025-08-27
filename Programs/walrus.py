#using walrus operators 

if(n := len([1 , 2, 3, 4, 5])) > 3:
    print("list is too long " , n , "elements, expected <=3 ")
    
    