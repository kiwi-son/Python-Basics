name="Jeet" #strings are immutable
#name[0]="s" #this will raise an error
a=len(name) #length of string
print(a)
text="Hello World"
print(text.lower()) #prints the string in lowercase
print(text.upper()) #prints the string in uppercase
print(text.capitalize()) #capitalizes first character of string

s="   Hello World   "
print(s.strip()) #removes leading and trailing whitespace 
print(s.lstrip()) #removes leading whitespace
print(s.rstrip()) #removes trailing whitespace  

s="Python is fun"
print(s.find("is")) #returns the index of first occurrence of substring
print(s.replace("fun","awesome")) #replaces a substring with another substring
print(s)

t="Apples, Bananas, Cherries"
print(t.split(", ")) #splits the string into a list of substrings based on a delimiter
print(",".join(["Apples", "Bananas", "Cherries"])) #joins a list of strings into a single string with a specified delimiter
print(text.count("o")) #counts occurrences of a substring in the string
print(text.startswith("Hello")) #checks if string starts with a specified substring
print(text.endswith("World")) #checks if string ends with a specified substring 


print(ord('A')) #returns the ASCII value of character
print(chr(65)) #returns the character corresponding to ASCII value
