
l1 = [1,4,7,8]
l2 = [2,5,7,23]

ans =0
for i in range(len(l1)):
	ans += l1[i]-l2[i]

print(abs(ans))

