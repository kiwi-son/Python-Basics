#Reading from a file
f=open("Jeet.txt", "r")
data=f.read()
print(data)
f.close()

#Writing to a file
f=open("Harry.txt","w")
string='''
Harry is a good person.
His favourite package is numpy.
'''
f.write(string)
f.close()

#Appending to a file
f=open("Harry.txt","a")
f.write("\nHe loves to code in python.")
f.close()

#Reading line by line
f=open("Harry.txt","r")
for line in f:
    print(line)