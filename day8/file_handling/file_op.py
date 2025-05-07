
fp = open('new_file.txt', 'w')

# w :: write mode
# It always open given file as empty file
# if file exists then contents are deleted
# if file doesn't exist then new file is created

# close file
fp.close()

# how to write into the file
# write function writes given string to the file
fp = open("new_file.txt", "w")
fp.write("Hello this is first line in this file")
fp.close()

# how to read the file
# open file in read mode
# Read mode :: allows to read the complete file

# read() :: read function reads all contents
# of the file in a single string
fp = open("new_file.txt", "r")
contents = fp.read()
print(contents)
fp.close()

# to add contents open file in append mode
fp = open("new_file.txt","a")
fp.write("\nHello this is second line in the file\n")
fp.close()


## BINARY FILE
# to read :: rb mode
# to write :: wb mode

##############################################################
# syntax for with construct
# close() function is always called

with open("new_file.txt", "r") as fp:
	contents = fp.read()
# when we come of with :: file is automatically closed by PVM
print(contents)

new_contents = "These are new contents \n next line"
with open("new_file.txt", "w") as fp:
	fp.write(new_contents)
# when we come of with :: file is automatically closed by PVM
print(contents)

