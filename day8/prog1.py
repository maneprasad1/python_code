
## sort list in descending order using lambda

l1 =[1,6,3,5,35,12]

def neg(n):
	return -n

sorted_l = sorted(l1, key=neg)
print(sorted_l)

sorted_l1 = sorted(l1, key = (lambda x: -x))
print(sorted_l1)
