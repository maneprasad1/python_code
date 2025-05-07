

l = [0,1,2,3,4,5]

for i in range(0,len(l),2):
	l[i],l[i+1]= l[i+1],l[i]

print(l)
