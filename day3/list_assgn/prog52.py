

def colordiff(c1, c2):
	l=[]
	for i in c1:
		if i not in c2:
			l.append(i)
	return l

color1 = ['white','red','orange','green','blue']
color2 = ['black','yellow','green','blue']

print(colordiff(color1,color2))
print(colordiff(color2,color1))

