# tell and seek method

f=open('student.txt', mode='r')
print(f.tell())
print(f.read())
print(f.seek(1))
print(f.tell())
f.close()
    