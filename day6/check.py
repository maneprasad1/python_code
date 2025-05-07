

s = input("Enter a string ")
s = s.lower()
print(s)
s = set(s)
s1 = set()
for i in range(97,123,1):
	s1.add(chr(i))

print(s1.issubset(s))
