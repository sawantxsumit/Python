#wap to find reverse of a given number 

class A():
    def reverse(self, x):
        sign = 1

        if x == 0:
            return 0
        
        if x < 0:
            sign = -1
            x = -x
        
        answer = 0

        while(x>0):
                answer=answer+x%10
                answer=answer*10
                x=x//10
        answer=answer//10
        answer = sign * answer

        if answer < (-2) ** 31 or answer > (2 ** 31) - 1 :
            return 0
        return answer




l=A()
n= int(input("enter a number :")) 
a=l.reverse(n)
print("Reverse of the number is :",a)
    
