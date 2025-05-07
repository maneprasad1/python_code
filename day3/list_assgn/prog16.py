
import math
l=[]
for i in range(200):
	if(math.sqrt(i)==int(math.sqrt(i))):
		l.append(i)
l = l[0:5]+l[-6:-1:]
print(l)
