num = int(input("Enter number"))
total = 0
while num>0:
	last = num%10
	num = num//10
	total += last
print(total)
