f=open('student.txt', mode='a')
size=int(input('enter list size :'))
for i in range(size):
    a=input('enter list element :')
    f.write(f'\n{a}')
f.close()
# print(f'sum of {a} and {b} is {sum}')