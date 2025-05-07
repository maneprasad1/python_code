
d = {'a':10,'b':20,'c':30,'d':40,'e':10}
tot = 0
l=[]

d_sort = sorted(d, key = (lambda x : d[x]))

print(d_sort[-3:])
