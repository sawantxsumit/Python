marks = {
    "sumit": 99,
    "rohan": 45,
    "ayush": 88,
    0: "hariom"
}

print(marks["sumit"])
print(marks["rohan"])
print(marks["ayush"])

#dictionary methods
print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"sumit": 100, "sawant": 89})
print(marks)
