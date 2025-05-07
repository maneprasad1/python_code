


l1 = [1,2,3,[400,500]]
l=[]
for i in l1:
	if type(i)==list:
		for j in i:
			l.append(j)

	else:
		l.append(i)
print(l1)
print(l)
