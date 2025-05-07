#!usr/bin/python3

marks = int(input("Enter your marks : "))

if marks>100:
	print("Enter below 100")
elif marks >80 :
	print("A")
elif marks>60:
	print("B")
elif marks>50:
	print("C")
elif marks>45:
	print("D")
elif marks>25:
	print("E")
elif marks>0:
	print("F")
else :
	print("Enter valid marks")
