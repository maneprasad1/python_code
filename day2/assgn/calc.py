import math
print("1.Add 2.Subtract 3.Divide 4.Multiply 5.Integer division 6.Mod operation",
"7.Check if same 8.Power 9.Square root 10.Log 11.GCD 12.LCM")
choice = int(input("Enter your choice "))
n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))

match choice:
	case 1:
		print("Addition ",n1+n2)
	case 2:
		print("Subtraction ", n1-n2)
	case 3:
		print("Divide ",n1/n2)
	case 4:
		print("Multiply ",n1*n2)
	case 5:
		print("Integer Division ",n1//n2)
	case 6:
		print("Modulus ", n1%n2)
	case 7:
		if n1==n2:
			print("Same")
		else:
			print("Not same")
	case 8:
		print("Power ", n1**n2)
	case 9:
		print("Square root ",math.sqrt(n1), math.sqrt(n2))
	case 10:
		print("Log ", math.log(n1), math.log(n2))
	case 11:
		print("GCD ", math.gcd(n1,n2))
	case 12:
		print("LCM ",math.lcm(n1,n2) )
	case _:
		print("Invalid input....")
