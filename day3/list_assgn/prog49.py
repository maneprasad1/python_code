
l1 =['Black','Red','Maroon','Yellow']
l2 =['#000000', '#FF0000', '#800000','#FFFF00']


l=[]
for i,j in zip(l1,l2):
	d={}
	d['color_name']=i
	d['color_code']=j
	l.append(d)

print(l)	
