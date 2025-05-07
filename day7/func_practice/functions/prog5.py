
def findfactorial(n):
	if n>=1:
		return n* findfactorial(n-1)
	else:
		return 1

n = int(input("Enter number "))
print(findfactorial(n))
