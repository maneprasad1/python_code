
def isPerfect(num):
	total = 0
	for i in range(1,num):
		if num%i == 0:
			total += i
	if total == num:
		print("Perfect number")
	else:
		print("Not perfect")
n = int(input("Enter number "))
isPerfect(n)
