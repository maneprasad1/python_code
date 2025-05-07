

string = input("Enter a string ")
n = len(string)

if n>=3:
	if string[-3:]=='ing':
		string += 'ly'
	else:
		string += 'ing'

print(string)
