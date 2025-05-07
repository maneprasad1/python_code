

n=int(input("Enter num of elements you want in list "))
l=[]
new=[]
for i in range(n):
	num = int(input("Enter element "))
	l.append(num)

for i in l:
	if i%2!=0:
		new.append(i)

print(l)
print(new)
