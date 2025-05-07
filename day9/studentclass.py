
class student:
	def __init__(self):
		self.name = input("Enter name ")
		self.rollno = int(input("Enter roll no "))
		self.marks1 = int(input("Enter marks 1 "))
		self.marks2 = int(input("ENter marks 2 "))
	def display(self):
		print(self.name, self.rollno,self.marks1,self.marks2)


stud1 = student()
stud1.display()
print(student.__dict__)
print(student.__doc__)
print(student.__name__)
print(student.__module__)
print(student.__bases__)
