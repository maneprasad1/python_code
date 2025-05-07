
print("Welcome to DBDA cafe...")
print("1.Tea 2.Coffee 3.Vadapav 4.Juice")
choice = int(input("Enter your choice"))

match choice:
	case 1:
		print("Price of tea - 12")
	case 2:
		print("Price of coffee - 25")
	case 3:
		print("Price of vadapav - 18")
	case 4:
		print("Price of Juice - 30")
	case _:
		print("Invalid input....")
