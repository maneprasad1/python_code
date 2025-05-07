
vowels = ['a','e','i','o','u']
words = ['abc','xyz','op','qwe']
l1 = []
l2 = []

for i in words:
	if i[0] in vowels:
		l1.append(i)
	else:
		l2.append(i)

print(l1)
print(l2)
