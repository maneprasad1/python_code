
string = input("Enter a string ")
if len(string)>=2:
	new = string[:2]+string[-2:]
	print(new)
else:
	print("")
