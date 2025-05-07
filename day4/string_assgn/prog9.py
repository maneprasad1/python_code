

string = input("Enter a string ")
n = int(input("Enter index to remove "))
s=''
for i in range(len(string)):
	if i != n:
		s += string[i]			
	else:
		continue

print(s)
