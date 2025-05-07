
n = int(input("Enter number "))
t = int(input("Enter terms "))
total = 1
i =1

while i<t :
	mul = 1
	j=i
	while j>0:
		mul = mul*j
		j = j-1		
	num = (n**i)/mul
	total += num
	i += 1

print(total)
	
