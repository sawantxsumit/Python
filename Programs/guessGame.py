from random import randint

num = randint(50 , 100)
guess =1

print("Guess a number between 50 and 100")
for i in range(1,10):   
    p = int(input("Enter the number :"))
    if(p == num ):
        print("Your guess is correct \nYou win")
        print(f"You took {guess} guesses")
        break
    elif(p< num):
        print("try a greater number ")
        print(f"you have {9-guess} guess left\n")
        guess+=1
    else:
        print("try a lower number ")
        print(f"you have {9-guess} guess left\n")
        guess+=1
    
    if(i==9):
        print("You ran out of GUESS \n better luck next time")
        print(f"the number was : {num}")

