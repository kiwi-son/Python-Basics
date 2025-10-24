a=int(input("Enter your lucky number"))

match a:
    case 1:
        print("Yeah! You won!")
    case 2:
        print("So close!, try again.")
    case 4:
        print("You won")
    case _:
        print("Better luck next time!")