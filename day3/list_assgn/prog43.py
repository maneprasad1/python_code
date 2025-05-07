
l = [12,23,34,45,56,67,99]

if len(l)%2!=0:
	first=l[:len(l)//2]
	sec = l[(len(l)//2):]
	print("first ",first)
	print("second ",sec)
else:
	print("first", l[:len(l)//2])
	print("second",l[len(l)//2:])
