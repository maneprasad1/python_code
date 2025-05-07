
d1 = {'a':100, 'b':200,'c':300}
d2 = {'a':300, 'b':200,'d':400}
d ={}
for i,j in zip(d1,d2):
	if i==j:
		d[i] = d1[i]+d2[j]
	else:
		d[i] = d1[i]
		d[j] = d2[j]
print(d)
