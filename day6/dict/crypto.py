
print(ord('a'))
print(ord('n'))
print(chr(ord('a')+13))
print(chr(ord('n')-13))

s = "Pnrfne"
s_list=list(s)

for i in s_list:
	if 78>=ord(i)>=65 or 110>=ord(i)>=97:
		s_list[i] = chr(ord(i)+13)
	else :
		s_list[i] = chr(ord(i)-13)

print("".join(s_list))
