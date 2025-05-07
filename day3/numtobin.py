

a = 6
s = ""
while a>0:
	if a%2!=0:
		s += '1'
	else :
		s+='0'
	a = a//2
print(s[::-1])
