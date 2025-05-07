
length = 0

for i in range(5):
	string = input("Enter word ")
	n= len(string)
	if n>length :
		word =  ''
		length = n
		word = string	
print(word)
print("Length ",length)
