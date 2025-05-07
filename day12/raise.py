
def func():
	try :
		a = 12/0
		print(a)
	except Exception as e:
		
		print("E")
		raise e
func()
