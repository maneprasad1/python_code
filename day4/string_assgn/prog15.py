
def add_tags(tag, word):
	s=''
	s+= "<{}>{}</{}>".format(tag,word,tag)
	print(s)

tag = input("Enter tag ")
word = input("Enter word ")
add_tags(tag, word)
