

n = int(input("Enter range "))
num = 0
total = 0
for i in range(n):
	num = 9*(10**i)+num
	total += num
print(total)
