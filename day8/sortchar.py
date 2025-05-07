
## sort first string char based on their pos in second string
# assume all chars of first string are in second string
# s1 = "IACSD"
# s2 = "ZDSAIKJLC"
# o/p  = [D,S,A,I,C]

s1 = "IACSD"
s2 = "ZDSAIKJLC"


sorted_l = sorted(s1, key = (lambda x : s2.find(x)))
print(sorted_l)
