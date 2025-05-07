
def squares(n):
	square_ls=[]
	for i in range(1,n+1):
		square_ls.append(i**2)
	print(square_ls)

n =int(input("Enter a number "))
squares(n)
