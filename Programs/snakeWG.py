
# snake =1
# water =-1
# gun =0
# snake vs water : snakes drinks water ->snake wins
# gun vs water : gun drowns in water -> water wins
# gun vs snake : gun kills the snake -> gun wins

import random
computer =random.choice([-1 , 1 ,0])

print("RULES OF THE GAME \n snake vs water : snakes drinks water ->snake wins\ngun vs water : gun drowns in water -> water wins\ngun vs snake : gun kills the snake -> gun wins")

str=input("SNAKE WATER or GUN \n choose one :")
dict={"snake" :1 , "water": -1 , "gun": 0}
revdict={value : key for key , value in reversed(dict.items())}
# method to reverse a dictionary
# reversedict={1:"snake"  , -1 :"water" , 0 :"gun"}
you=dict[str.lower()]
print("computer chose" , revdict[computer])
# if(computer == you):
#     print("\nDRAW \n try again ")    
# elif(computer ==-1 and you ==1): 
#     print("\nyou win")
# elif(computer== -1 and you ==0):
#     print("\nyou lose ") 
# elif(computer== 1 and you ==0):
#     print("\nyou win") 
# elif(computer== 1 and you ==-1):
#     print("\nyou lose") 
# elif(computer== 0 and you ==-1):
#     print("\nyou win") 
# elif(computer== 0 and you ==1):
#     print("\nyou lose") 


# another logic
if((computer - you)== -1 or (computer - you)== 2):
    print("you lose")
else:
    print("you win")
    


