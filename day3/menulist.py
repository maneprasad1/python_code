import math
l = [10,20,30,40,50,60,70]
print(l)
print("1.Reverse 2.Print center 3.First 2 elements 4.Last 2 elements 5.Square root")
choice =int(input("Enter your choice"))

match choice :
	case 1:
		print("Reversed list - ", l[::-1])
	case 2:
		print("Center element - ", l[len(l)//2])
	case 3:
		print("First two elements - ", l[:2])
	case 4:
		print("Last two elements - ", l[-2:])
	case 5:
		for i in l:
			print(math.sqrt(i))
	case _:
		print("Invalid input...")
