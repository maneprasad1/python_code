
first = ['b','a','c','d','e','f']
second = ['d','e','f','g','h']
missing=[]
additional=[]
for i in second:
	if i not in first:
		additional.append(i)
for i in first:
	if i not in second:
		missing.append(i)

print(missing)
print(additional)
