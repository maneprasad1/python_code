
data = [{'V':'S001'},{'V':'S002'},{'VI':'S005'},{'VII':'S005'},{'V':'S009'},
	{'VIII':'S007'}]
output = set()

for i in data:
	for j in i:
		output.add(i[j])

print(output)
