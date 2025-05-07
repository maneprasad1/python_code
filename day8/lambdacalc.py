
print("1.Addition 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter your choice "))

x = int(input("Enter first number "))
y = int(input("Enter second number "))
match choice:
	case 1:
		(lambda x,y : print(x+y))(x,y)
	case 2:
		(lambda x,y : print(x-y))(x,y)	
	case 3:
		(lambda x,y : print(x*y))(x,y)
	case 4:
		(lambda x,y : print(x/y))(x,y)
	case _:
		print("Invalid choice")
