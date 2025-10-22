#The input function allows user to take the input
#It always takes input in string format
name=input("Enter your name: ")
print("Your name is:",name)
a=int(input("Enter first number: ")) #typecasting input to integer
b=int(input("Enter second number: ")) #typecasting input to integer 
print("Sum is:",a+b)

#f string allows to embed expressions inside string literals, using curly braces {}
age=int(input("Enter your age: "))
print(f"My name is : {name} Your age is: {age}")