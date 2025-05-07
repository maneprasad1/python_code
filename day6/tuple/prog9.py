
tup1 = (1,2,3,4,4,2,4,3,5)
l1 = []
dup = []
for i in tup1:
	if i not in l1:
		l1.append(i)	
	elif i not in dup:
		dup.append(i)

print(dup)
