
l1 = [1,2,3,4,5,6,7,8]
l2 = [2,4,6,8,10]
l =[]
if len(l1)>len(l2):
	for i in l2:
		if i in l1:
			l.append(i)
else:
	for i in l1:
		if i in l2:
			l.append(i)

print(l)
