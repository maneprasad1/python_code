
string = input("Enter a string ")
s_list = string.split(" ")
s_set=set(s_list)
d ={}
for i in s_set:
	d[i] = s_list.count(i)
print(d)
