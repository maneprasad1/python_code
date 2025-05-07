
a = int(input("Enter first number"))

b = int(input("Enter second number"))
print("1.ADD 2.SUBTRACT 3.MULTIPLY 4. DIVIDE")

choice = int(input("Enter your choice"))

match choice:
	case 1:
		print("addition - ",a+b)
	case 2:
		print("Subtraction - ", a-b)
	case 3:
		print("Multiply - ",a*b)
	case 4:
		print("Divide - ",a/b)
	case _:
		print("Invalid input....")
