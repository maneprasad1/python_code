cnt = 0
total = 0
while cnt<20:
	num = int(input("enter number "))
	if num%2 == 0:
		total += num
	cnt +=1
print(total)
