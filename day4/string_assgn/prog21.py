
def convertupper(s):
	cnt = 0
	for ch in s[:4]:
		if ch.isupper():
			cnt +=1
		if cnt>=2:
			return s.upper()
	else:
		return s
s = input("Enter string ")
print(convertupper(s))
