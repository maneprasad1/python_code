
l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
for i in range(len(l1)-2):
	if l1[i]+1==l1[i+1] and l1[i]+2==l1[i+2]:
		print([l1[i],l1[i+1],l1[i+2]])
