

def splitlist(l,n):
	b=[]
	for i in range(n):
		a=[]
		for j in range(i, len(l),n):
			
			a.append(l[j])
		b.append(a)
	return b

l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
n = 3

print(splitlist(l1,n))
