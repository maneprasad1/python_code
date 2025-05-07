
s = {1,2,3,4,2,4}
s1 = s
s2 = s
s.clear()

for i in range(len(s1)):
	s1.pop()
for i in s2.copy():
	s2.remove(i)

print("S",s)
print("s1",s1)
print("s2",s2)
