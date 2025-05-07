
def startstr(s, ch):
	if s[0] == ch:
		print("starts with specified char")
	else:
		print("Does not start with specified char")

s= 'prasad'
ch = 'p'
startstr(s,ch)
print(s.startswith(ch))
