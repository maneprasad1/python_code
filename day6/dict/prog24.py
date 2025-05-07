
sample = 'w3resource'
setstr = []
for i in sample:
	if i not in setstr:
		setstr.append(i)

d = {}

for i in setstr:
	d[i] = sample.count(i)

print(d)
