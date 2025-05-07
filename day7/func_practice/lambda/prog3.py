
list1 = [('English',88),('Science',90),('Maths',97),('Social Sciences',82)]

sort_tuple = sorted(list1, key = (lambda x : x[1]))
print(sort_tuple)
