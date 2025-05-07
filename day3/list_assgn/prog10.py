

def longer_words(list1,n):
	long_list=[]
	for w in list1:
		if len(w)>n:
			long_list.append(w)
	return long_list

list1 = ['abf','fadawe','parsad','ge','efwh']
n = 3
print(longer_words(list1,n))
	
