

l1 = [1,2,3]
res =[]
for i in range(len(l1)):
	for j in range(i+1, len(l1)+1):
		res.append(l1[i:j])

print(res)
