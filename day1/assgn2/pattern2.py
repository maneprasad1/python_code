


n = int(input("Enter number"))

for i in range(1,n+1,2):
	print(' '*(n-i)+'*'*i)

for i in range(n-2,0,-2):
	print(' '*(n-i)+'*'*i)

