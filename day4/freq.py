
string = 'google.com'
a = ''
for i in string:
	if i not in a:
		a+=i

for i in a:
	print(i ,string.count(i), end=',')
