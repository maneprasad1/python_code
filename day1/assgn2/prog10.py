

n = int(input("Enter number "))
t = int(input("Enter terms "))

total = 0
i = 1
r = 1
while i<=t:
	if (i%2!=0):
		num = n**r
		print(num)
	else:
		num = -(n**r)
		print(num)
	total += num
	r += 2
	i+=1
print(total)
