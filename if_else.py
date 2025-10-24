age=22
guess=int(input("Guess my age: "))
if guess==age:
    print("Congratulations! You guessed it right age.")
elif guess<age:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")

print("End of the program.")