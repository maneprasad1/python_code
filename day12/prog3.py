# file handling error

try:
	with open("Temp1.txt", "r") as fp:
		print("File opened")
except FileNotFoundError:
	print("File not found")
	print("Creating a file...")
	fp = open("Temp1.txt", "w")
	fp.write("Hello")
	
	fp.close()
print("Completed")
