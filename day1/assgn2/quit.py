total = 0
mult = 1
flag = 1
cnt = 0
while flag:
	num = int(input("enter number"))
	cnt +=1
	total +=  num
	mult *= num
	quit = input("Press q to quit")
	if quit == 'q':
		flag = 0
print("average ", total/cnt)
print("product ", mult)
