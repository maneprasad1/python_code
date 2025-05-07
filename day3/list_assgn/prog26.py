


l1=[1,2,3,4]
l2=[2,3,4,1]
l3 = l2*2

for i in range(len(l1)):
	if l1 == l3[i:i+4]:
		print("True")
		break
else:
	print("False")	
