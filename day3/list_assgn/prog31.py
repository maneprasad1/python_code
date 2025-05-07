

start = int(input("Enter start index "))
end = int(input("Enter end index "))

if (start<0 and end <0) and start<end:
	print(abs(end-start))
elif (start>0 and end >0) and start<end:
	print(end-start)
else:
	print("Invalid index")
