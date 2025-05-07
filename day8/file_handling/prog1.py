
with open("sample_file.txt","r") as fp:
	contents = fp.read()

print(contents)

###################################

n = 5
with open("sample_file.txt","r") as fp:
	contents = fp.read()

lines = contents.split('\n')

print(lines[:5])

#################################

with open("sample_file.txt","a") as fp:
	fp.write("Bye BYe ")
with open("sample_file.txt","r") as fp:
	contents = fp.read()
print(contents)

################################

with open("sample_file.txt","r") as fp:
	contents = fp.read()

lines = contents.split('\n')

print(lines)
