

def combine(list1):
	d = {}
	for i in list1:
		if i['item'] not in d:
			d[i['item']] = i['amount']
		else:
			d[i['item']] += i['amount']
	return d

data = [{'item':'item1', 'amount':400}, {'item':'item2', 'amount':300},
{'item':'item1', 'amount':750}]

ans = combine(data)
print(ans)
