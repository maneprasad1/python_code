
def hyphen(s):
	words = s.split("-")
	words.sort()
	print("-".join(words))

s = "green-red-yellow-black-white"
hyphen(s)
