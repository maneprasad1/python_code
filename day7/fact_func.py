

def factorial(n):
	fact = 1
	while n>0:
		fact = fact*n
		n=n-1
	print(fact)

n = int(input("Enter number "))
factorial(n)
