
prompt = print("1.Addition 2.Subtraction 3.Multiply 4.Division")
choice =int(input("Enter your choice "))

def add(a,b):
	print(a+b)
def sub(a,b):
	print(a-b)
def mul(a,b):
	print(a*b)
def div(a,b):
	print(a/b)
a = int(input("Enter first number "))
b = int(input("Enter second number "))
match choice:
	case 1:
		add(a,b)
	case 2:
		sub(a,b)
	case 3:
		mul(a,b)
	case 4:
		div(a,b)
	case _:
		print("Invalid choice !!!")
