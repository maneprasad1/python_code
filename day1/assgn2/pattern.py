
n = int(input("Enter number of lines "))

for i in range(1,n+1):
	print('*'*i)

print('@'*50)
for i in range(1,n+1):
	print('*'*(i*2-1))
print('@'*50)
for i in range(1,n+1):
	print('*'*i*2)
