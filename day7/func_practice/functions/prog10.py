
def evenlist(list1):
	even_list=[]
	for e in list1:
		if e%2==0:
			even_list.append(e)
	print(even_list)

list1 = [1,2,3,4,5,6,7,8,9]
evenlist(list1)
