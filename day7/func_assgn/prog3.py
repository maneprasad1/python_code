
def isPalindrome(s):
	if s == s[::-1]:
		return 1
	else:
		return 0

s = "amam"
ans = isPalindrome(s)
print(ans)
