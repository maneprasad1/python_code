

def iskeyid(dict):
	for d in dict:
		if 'id' in d:
			print(d)

d = [{'id':1},{'id':23,'name':'ava'},{1:2,3:'id'},{1:2}]
iskeyid(d)
