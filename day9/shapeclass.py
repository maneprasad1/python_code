
#create class shape
#attrs :- height, width,length
#display - instance method
#display_count --> class method
#stretch --> static method
class shape:
	def __init__(self):
		self.height = 10
		self.width = 20
		self.length = 100
	def display(self):
		print(self.height, self.width,self.length)
	@classmethod
	def display_count(cls):
		print("This is class method")
	@staticmethod
	def stretch():
		print("This is static method")

shape1 = shape()
##call instance method
shape1.display()
#shape.display() #error

#call class method
shape.display_count()
shape1.display_count()

#call static method
shape.stretch()
shape1.stretch() #error in older version


