
def lastthree(s):
	if len(s)<3:
		return s
	else:
		return s[:3]

s = input("Enter string ")
print(lastthree(s))
