
def countLowerUpper(s):
	lower_cnt = 0
	upper_cnt = 0
	for char in s:
		if char.islower():
			lower_cnt += 1
		elif char.isupper():
			upper_cnt += 1
	print("No of uppercase chars ",upper_cnt)
	print("No of lowercase chars ",lower_cnt)

s = "The quick Brown Fox"
countLowerUpper(s)
