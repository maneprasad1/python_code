
num = int(input("Enter number to check if its prime"))

n= 2
while n<num:
	if num%n==0:
		print("Not Prime")
		break
	n+=1
else:
	print("Prime")
