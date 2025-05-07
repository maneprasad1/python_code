
def printname(dict):
	if 'rollno' in dict:
		if dict['rollno']==100:
			print(dict["name"])

d = {'name':'prasad', 'rollno':100}
printname(d)
