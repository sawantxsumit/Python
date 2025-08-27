
def main():
    try:
        a=int(input("Enter a number :"))
        print(a)
        return
        
    except Exception as e:
        print(e, "\nEnter an integer please")
        return

    finally:
        print("we are inside finally block")
    
    
# finally runs in both try and except cases 
#finally is executed even when it is used in a function and even after a return is executed in the function

main()