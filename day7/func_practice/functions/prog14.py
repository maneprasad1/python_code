
def pangrams(s):
	alpha=set()
	for i in range(97,123):
		alpha.add(chr(i))
	
	s1= set(s.lower())
	if s1.issuperset(alpha):
		print("It is pangram")
	else:
		print("NOt a pangram")

s = "The quick brown fox jumps over the lazy dog"
pangrams(s)
