
def reversestring(s):
	if len(s)%4==0:
		return s[::-1]
	else:
		return s

s = input("Enter a string ")
print(reversestring(s))
