

s= input("Enter a string ")
ni = s.find("not")
pi = s.find("poor")
if (ni != -1) and (pi != -1) and (ni<pi):
	s = s[:ni]+"good"+s[pi+4:]

print(s)





'''
string = input("Enter string ")

words = string.split(" ")

for i in range(len(words)):
	if words[i]=='not':
		n = i
	if words[i]=='poor':
		p = i
		break
	
if  n<p:
	words.insert(n,'good')

print(words)
s = " ".join(words)
print(s)

'''


