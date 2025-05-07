
n = int(input("Enter number of lines"))
for i in range(n,0,-1):
	print(" "*(n-i), end = '')
	for j in range(i*2-1):
		if j%2==0:
			print("1", end="")
		else:
			print("0", end="")
	print()

