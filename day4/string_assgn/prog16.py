
def insert_string_middle(s1,s2):
	s =''
	s += "{}{}{}".format(s1[:len(s1)//2],s2, s1[len(s1)//2:])
	print(s)

s1 = input("Enter string 1 ")
s2 = input("Enter string 2 ")
insert_string_middle(s1,s2)
