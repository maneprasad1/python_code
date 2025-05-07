

def lastpart(s,ch):
	return s.rsplit(ch,1)[0]


s = input("enter string ")
ch = input("Enter character before which you want string ")
print(lastpart(s,ch))
