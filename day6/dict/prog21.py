import itertools
data = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
l1 = []
for i in data:
	l1.append(data[i])

res = itertools.product(*l1)
for i in res:
	print("".join(i))
