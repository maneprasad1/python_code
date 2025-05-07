
# find unique words in sentence and their count
##wap to take 5 numbers from user in comma seperated format 
# print non repeated numbers

n = input("Enter 5 numbers comma seperated ")

num =n.split(',')
s1 = set()
for i in num:
	num =int(i)
	s1.add(num)

print(s1)
