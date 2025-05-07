
class person:
	population = 0
	def __init__(self):
		self.name = input("Enter name ")
		self.weight = float("Enter weight ")
		self.heigth = float("Enter heigth ")
		self.age = float("Enter age")
	def increase_population(cls): # class method
		person.population += 1
	def display(self):
		print(self.name, self.weigth,self.heigth,self.age)

p1 = person()
