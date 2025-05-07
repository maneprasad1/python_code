
n = int(input("Enter number of terms to be generated"))

i=0
total = 0
num = 0
while i<n:
	num = 9*(10**i)+num
	total += num
	i += 1
print("Total : ",total)
