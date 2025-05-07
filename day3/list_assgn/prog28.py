

l = [1,2,3,4,5,5,10,0]

largest = 0
large_2nd = 0

for i in l:
	if i>largest:
		large_2nd = largest
		largest = i
	if i>large_2nd and i<largest:
		large_2nd = i

print("2nd largest  ", large_2nd)
		
