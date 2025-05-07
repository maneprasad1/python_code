
d ={}
for i in range(5):
	key = input("Enter employee id ")
	value = input("Enter employee value ")
	d[key] = value

sort_dict = sorted(d)
sort_emp ={}
for k in sort_dict:
	sort_emp[k] = d[k]
print(sort_emp)
sort_dict = sorted(d, key = (lambda x : d[x]))
sort_name = {}
for k in sort_dict:
	sort_name[k]=d[k]
print(sort_name)
