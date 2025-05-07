

n = int(input("Enter num of elements you want in list "))
l=[]
for i in range(n):
	num = input("Enter element ")
	l.append(num)
unique=[]
for i in l:
	if i not in unique:
		unique.append(i)

print(sorted(unique))
