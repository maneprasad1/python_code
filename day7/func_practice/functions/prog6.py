

def inRange(num,start,end):
	if start<num<end:
		print("In range")
	else:
		print("Not in range")

num = int(input("Enter number "))
start = int(input("Enter start "))
end = int(input("Enter end "))
inRange(num,start, end)
