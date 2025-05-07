
def sortstring(s):
	#return sorted(s)
	s = list(s)
	for i in range(len(s)):
		for j in range(i):
			if s[j]>s[i]:
				s[j],s[i] = s[i],s[j]
	return s
print(sortstring('prasad'))

