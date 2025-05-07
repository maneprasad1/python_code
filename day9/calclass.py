# calculator class add, sub,mul,div

class calc:
	@staticmethod
	def add(a,b):
		return a+b
	@staticmethod
	def sub(a,b):
		return a-b
	@staticmethod
	def mul(a,b):
		return a*b
	@staticmethod
	def div(a,b):
		return a/b

c1 = calc()
print(c1.add(3,2))
