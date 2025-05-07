
def pascaltriangle(n):
	prev = [1]
	print(prev)
	curr=[]
	for row_no in range(n):
			curr.append(1)
			for j in range(1,len(prev)):
				curr.append(prev[j]+prev[j-1])
			curr.append(1)
			print(curr)
			prev = curr
			curr=[]

pascaltriangle(5)
