
string = input("Enter a string ")

l = string[0]
new_s=l
for i in range(1,len(string)):
	if string[i]==l:
		new_s += '$'
	else:
		new_s += string[i]	
print(new_s)
