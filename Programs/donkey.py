censor=["donkey" , "bad" , "hard"]

with open("donkey.txt") as f:
    content= f.read()

for items in censor:
    content = content.replace(items, "#" *len(items))

with open("donkey.txt" , "w") as f:
    f.write(content)

