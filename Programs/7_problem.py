import random

def game():
    print("you are playing the game ")
    score=random.randint(1,100)
    
    # fetch the high scores
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
            # since f.read reads the value as a string thus we have to convert it into an integer        
        else:
            hiscore=0
    print("your score :" , score)
    if(score > hiscore):
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))
            # write argument must be a string 
            # thus we have to typecast score as string
    
    return score

game()