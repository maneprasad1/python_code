
n = int(input("Enter number "))

if n>100:
	print("Not more than 100 digits")
elif n<0:
	print("Please enter a positive number")
else:
	a = 0
	b = 1	
	if n==1:
		print(a)
	elif n==2:
		print(a,b, sep="|")
	else:
		print(a,b, sep="|", end="|")
		for i in range(n-2):
			c = a+b
			print(c, end="|" )
			a=b
			b=c

