




l = [1,1,2,3,3,5,4,23,4,3,1]
l1 =[]
for i in l:
	if i not in l1:
		l1.append(i)

for i in range(len(l1)):
	print(l1[i], l.count(l1[i]))
