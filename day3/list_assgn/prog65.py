
l = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
l1 =[]

zero=l.count(0)
for i in range(zero):
	l.remove(0)

l.extend([0]*zero)
print(l)
