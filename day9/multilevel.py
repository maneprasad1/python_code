# Multi level inheritance

class Person:
	def __init__(self):
		self.name = input("Enter your name ")

class Employee(Person):
	def __init__(self):
		super().__init__() # parent class __init__
		self.eid = int(input("ENter your employee id "))
	def display(self):
		print(self.name, self.eid)

class Manager(Employee):
	def __init__(self):
		Employee.__init__(self) # employee class init
		self.team_size = input("Enter team size ")

e1 = Employee()
e1.display()
m1 = Manager()
m1.display()
