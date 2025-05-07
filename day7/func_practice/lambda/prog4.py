
dict = [{'make':'Nokia','model':216,'color':'Black'},
	{'make':'Mi Msx','model':2, 'color':'Gold'},
	{'make':'Samsung','model':7,'color':'Blue'}]

sort_dict = sorted(dict, key = (lambda x : x['color']))
print(sort_dict)
