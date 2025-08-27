def func():
    print("hello sumit")
    
# func()
# print(__name__)

if __name__=="__main__":
    #everything written under this block will not be executed when run by importing this file
    print("this is the main module file")
    print(__name__)