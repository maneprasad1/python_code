
s1 = input("Enter first number")
s2 = input("Enter second number")

try:
	float(s1) and float(s2)
except ValueError:
	print("NO float")
	raise TypeError


l1 = s2.split(".")
ans = "".join(l1)
if ans.isdigit()==False:
	raise TypeError
