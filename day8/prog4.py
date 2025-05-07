

def name(new_list):
	return new_list[1]

l = ['prasad','shubh','vivek','rushi', 'prasad','vivek']
set_emp = set(l)
new_list = list(set_emp)
# normal function
sorted_emp = sorted(new_list, key = name)
print(sorted_emp)
# using lambda
sorted_emp = sorted(new_list, key = lambda x : x[1])

