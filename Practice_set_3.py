"""
Create a string variable name with your full name. Print:

The first character
The last character
The length of the string
"""

name="Jeet Sadhukhan"
print(name[0])  # First character
print(name[-1]) # Last character
print(len(name)) # Length of the string

"""
Concatenate two strings: "Hello" and "World" with a space in between.

"""
print(" ".join(["Hello","World"]))

"""
Reverse the string text using slicing.

"""

text = "Python Programming"
r=text[::-1]
print(r)

"""
Take the string "  i love python programming  " and:

Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
"""
s = "  i love python programming  "
p=s.strip()
print(p)
print(p.title())
print(p.count("o"))

"""
Write a program that counts how many vowels are in a given string.
"""
p="abc,abckc,c.nc.ksdfkgwlfj;jfqvdlfjwejvm.lergh"
print(p.count('a')+p.count('e')+p.count('i')+p.count('o')+p.count('u'))

"""
Take a user input string and check if it is a palindrome (same forwards and backwards).
"""

user_input = input("Enter a string: ")
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")