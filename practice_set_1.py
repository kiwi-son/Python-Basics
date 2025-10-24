""" Q1: Your First Program
Write a program that prints:
Hello, World! Welcome to Python."""

print("Hello, World! Welcome to Python.")

""""Q2: Print a Poem
Write a program that prints 
the following poem using a single print() statement:

Twinkle, twinkle, little star,
How I wonder what you are!"""
print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

"""Q3: Variables & Data Types
Create variables to store: - Your name (string)
- Your age (integer)
- Your height in meters (float)
- A boolean value representing whether you are a student
Print all of them in one line. """

name="Jeet"
age=22
height=1.75
is_student=False

print(f"My name is {name}, I am {age} years old, my height is {height} meter and it is {is_student} that I am a student")

"""Q4: num = "45"
Convert it into an integer and add 10 to it. Print the result.

"""
num="45"
print(int(num)+10)

"""Q5: Taking User Input
Write a program that:
Asks the user for their favorite food.
Prints:
Your favorite food is: <food>
"""
Food=input("Enter your favorite food:  ")
print("Your favorite food is:",Food)

"""Q7: Escape Sequences
Print the following output using escape sequences:
Harry said, "Python is awesome!"
This is on a new line.
This is a tab -> <- here
"""
print("Harry said, \"Python is awesome!\"\nThis is on a new line.\nThis is a tabe \t here")

"""Q8: Operator Challenge
Write a program that:
Takes an integer as input from the user.
Prints the square and cube of that number.
"""
num=int(input("Enter a number: "))
print("Square is:", num**2)
print("Cube is: ",num**3 )

