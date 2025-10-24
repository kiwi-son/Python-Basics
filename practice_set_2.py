""""
1. If-Else Conditional Statements
Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
Create a program that checks if a person is eligible to vote (age >= 18).
Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
"""
num = int(input("Enter a number: "))

#Whether the number is positive, negative or zero
if num>0:
    print("The  number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

#Check voting eligibility
if num>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Check whether the number is even or odd
if num%2==0:
    print("Even")
else:
    print("Odd")

"""
Ask the user to enter a day number (1–7) and print the corresponding day of
the week using match case .
Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case .
"""
#day number to day name
a=int(input("Enter a day numnber (1-7): "))
match a:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")   
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

#Simple calculator
num1=int(input("Enter your first integer number"))
num2=int(input("Enter your second integer number"))
oper=input("Enter the operation (+,-,*,/):")
match oper:
    case '+':
        print("The sum is :", num1+num2)
    case '-':
        print("The differnece is :", abs(num1-num2))
    case '*':
        print("The product is :", num1*num2)
    case '/':
        if num2!=0:
            print("The quotient is :", num1/num2)
        else:
            print("Division by zero is not allowed")
    case _:
        print("Invalid operation")

"""
Print numbers from 1 to 10 using a for loop.
Print the multiplication table of a number (entered by user).
Calculate the sum of all numbers from 1 to 100 using a for loop.
Print the following pattern using a for loop:
*
**
***
****
"""
#Print numbers from 1 to 10
for i in range (1,11):
    print(i)
#Multiplication table of a number
num=int(input("Enter a number to print its multiplication table: "))
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")
#Sum of all numbers from 1 to 100
sum=0
for i in range(1,101):
    sum+=i
print(sum)
#Print pattern
num=int(input("Enter a number"))
for i in range (1,num+1):
        print("*"*i)

"""
Write a program that keeps asking the user to enter a password until they
enter the correct one.
Use a while loop to reverse a given number (e.g., 123 → 321).
"""
password="abcd"
pas=input("Enter the password")
while pas!=password:
    print("Wrong password!")
    pas=input("Enter the password")

print("Password accepted")

#Reverse a given number
num=int(input("Enter the number"))
rev=0
while(num>0):
    r=num%10
    rev=(rev*10)+r
    num=num//10

print(rev)