with open("poem.txt") as f:
    content=f.read()
    if("twinkle" in content.lower()):
        print("the word twinkle is present in the poem file")
    else:
        print("twinkle is not present")