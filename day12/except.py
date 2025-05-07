
def func1_handle(a,b):
	try:
		c = a/b
		print(c)
	except ZeroDivisionError:
		print("There is zero division error")
	except ArithmeticError:
		print("Arithmetic Error")
	except Exception:
		print("There is a problem")

print("Calling func1")
func1_handle(10,10)
print("Completed")
