
def inf_seq():
	num = 0
	while True:
		yield num
		num += 1

iseq = inf_seq()
for i in range(10):
	print(next(iseq))
