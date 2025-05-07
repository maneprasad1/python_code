
l =[]
n =int(input("Enter length of list")) 
for i in range(n):
	n = int(input("Enter value"))
	l.append(n)
flag = 1
for i in l:
	if i==1:
		flag = 0
		break
	for j in range(2,i):
		if i%j==0:
			flag=0
			break

print(bool(flag))
