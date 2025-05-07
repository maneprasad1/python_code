
s = input("Enter string ")

for i in s:
	if (65<=ord(i)<=90)or (97<=ord(i)<=122):
		pass
	else:
		print("Not alpha")
		break
else:
	print("alalpha")  


for i in s:
	if ('a'>=i>='z') or ('A'>=i>='Z'):
		print("Not alpha")
		break
else:
	print("alpha")
