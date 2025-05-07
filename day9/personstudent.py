
class person:
	def __init__(self):
		self.name = input("Enter your name ")
	
class student:
	def __init__(self):
		person.__init__(self)
		self.rollno = input("Enter roll no ")
		self.marks =input( "Enter marks ")
		self.course = input("Enter course ")
		self.skills = input("Enter skills ")
	def display(self):
		print(self.name, self.rollno, self.marks)

s1 = student()
s1.display()
