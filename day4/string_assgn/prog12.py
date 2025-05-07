

string = input("Enter a sentence ")
words = string.split(" ")

unique = []

for i in words:
	if i not in unique:
		unique.append(i)
for i in unique :
	print(i, words.count(i))
