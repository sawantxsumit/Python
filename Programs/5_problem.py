def rem(l , word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l=["sumit" , "ayush" , "abhishek " , "pankaj" , "rohan" , "an"]

print(rem(l ,"an"))