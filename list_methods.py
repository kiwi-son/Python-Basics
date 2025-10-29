marks=[5,23,4,6,7]
marks.append(63)
print(marks)
marks[2]=45
print(marks)
marks.pop()
print(marks)
marks.insert(1,99)
print(marks)
extra_marks=[12,34,56]
marks.extend(extra_marks)
print(marks)
marks.sort()
print(marks)
marks.append(23)
print(marks.count(23))
marks.remove(23)#removes first occurrence
print(marks)

#create a list containing the table of 5
table=[x*5 for x in range(1,11)]
print(table)