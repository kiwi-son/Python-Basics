"""
Create a list fruits = ["apple", "banana", "cherry"].

Print the first fruit.
Replace "banana" with "orange".
Print the length of the list.
Create a list of numbers from 1 to 10.

Print the first three numbers using slicing.
Print the last three numbers using slicing.
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[fruits.index("banana")] = "orange"
print(fruits)
print(len(fruits))

l=[i for i in range(1,11)]
print(l[:3])
print(l[-3:])


"""
Start with numbers = [5, 2, 9, 1, 7] and do the following:

Sort the list in ascending order.
Append the number 10 to the list.
Remove the number 2 from the list.
Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.
"""
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)
"""
Create a tuple coordinates = (10, 20) Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
"""
co=(10,20)
l=list(co)
print(l)
l[0]=50
co=tuple(l)
print(co)

"""
Write a program that merges two dictionaries into one.
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)