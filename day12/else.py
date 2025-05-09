
def func1():
	try:
		print("in try")	
		return 1
	except:
		print("In except")
		return 2
	else:
		print("In else")
	finally:
		print("in finally")
		return 4
print(func1())
