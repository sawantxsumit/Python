# x^n using lambda

# power= lambda x , n: x**n
# print(power(2,4))

#factorial usinng recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))