
d = {'a':1,'b':2,'c':2,'d':4,'e':4,'f':5}
dict={}
for elem in d.copy():
	if d[elem] not in dict.values():
		dict[elem]= d[elem]

print(dict)
