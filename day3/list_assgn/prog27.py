

l = [3,4,5,6,3.5]
smallest = max(l)
small_2 = 0

for i in l:
	if i<smallest:
		small_2 = smallest
		smallest = i
	if i<small_2 and i>smallest:
		small_2 = i
print(small_2)
