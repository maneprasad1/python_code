
ip = [1,2,3,4]
d={}

for i in range(len(ip)-1, -1,-1):
	arr=d
	d={}
	d[ip[i]] = arr
	
print(d)

new = curr = {}
for i in ip:
	curr[i] = {}
	curr = curr[i]
	print(curr)
	print(new)
print(new)
print(curr)
