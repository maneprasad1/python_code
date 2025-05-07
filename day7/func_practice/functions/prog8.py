
def distinctlist(list1):
	l = []
	for e in list1:
		if e not in l:
			l.append(e)

	print(l)

list1 =[1,2,3,3,3,3,4,4,5]
distinctlist(list1)
