

print("1.Binary 2.Octal 3.Hex")
choice  = int(input("Enter choice number"))

match choice:
	case 1 :
		n = input("Enter binary string ")
		print(int(n, base=2))
	case 2 :
		n = input("Enter Octal string ")
		print(int(n, base=8))
	case 3 :
		n = input("Enter Hex string ")
		print(int(n, base=16))
	case _:
		print("Invalid input")
