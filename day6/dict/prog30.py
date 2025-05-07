
ip = {'item1':45.50, 'item2':35, 'item3':41.30, 'item4':55, 'item5':24}

sorted_d = sorted(ip, key = lambda x : ip[x], reverse = True)

for i in sorted_d[:3]:
	print(i, ip[i])
