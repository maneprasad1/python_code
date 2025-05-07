
n = input("Enter binary string")
cnt_0 = 0
cnt_1 = 0

for i in range(2,len(n)):
	if n[i]=='1':
		cnt_1 += 1
	elif n[i]=='0' :
		cnt_0 +=  1

print("Total 0 ", cnt_0)
print("Total 1 ", cnt_1)
