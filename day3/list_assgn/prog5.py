

def count_strings(liststr):
	cnt = 0
	for s in liststr:
		if len(s)>=2 and s[0]==s[-1]:
			cnt += 1
	return cnt

list1 = ['abc','xyz','aba','1221'] 
print(count_strings(list1))
