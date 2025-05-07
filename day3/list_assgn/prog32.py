
l1 = [5,7,9,12]
l2 = [2,7,9]

for i in l2:
	if i not in l1:
		print("Not a sublist")
		break
else:
	print("Sublist")
