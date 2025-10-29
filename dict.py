marks ={
    "harry": 98,
    "rohan": 67,
    "Jeet": 78
}

print(marks["harry"])
marks["harry"] = 99 #updating value
print(marks["harry"])
marks["yshan"]=87 #adding new entry
print(marks)

print(marks.keys())
print(marks.values())
print(marks.items())
for item in marks.items():
    print(item)
for key, value in marks.items():
    print(f"key is {key} and value is {value}")

