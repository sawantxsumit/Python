# wap to print vowels and consonant in a given string

s="hello how are you today"

vowels=['a', 'e' , 'i' , 'o' ,'u']
v=[]
c=[]
vow, con=0,0
s=s.replace(" ","")
# s=s.strip() #only removes leading and trailing whitespaces
for char in s:
    if char in vowels:
        v.append(char)
        vow+=1
    else :
        c.append(char)
        con+=1

#method 2
# con,vow=0,0
# vowels=['a', 'e' , 'i' , 'o' ,'u']

# for i in range(len(s)):
#     if s[i] in vowels:
#         vow+=1
#     elif(s[i]==" "):
#         pass
#     else:
#         con+=1
print(vow)
print(con)
print("vowels :",v)
print("consonants :",c)