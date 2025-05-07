
l1=[90,98,87,76,65]
n =int(input("Enter index "))
if len(l1)-1 >= n>0 :
	print("Exists")
elif n<0 and len(l1)>=abs(n):
	print("Exists")
else:
	print("Out of bound index")
