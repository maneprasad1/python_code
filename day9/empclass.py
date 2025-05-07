
class employee:
	cname = input("Enter company name ")
	def __init__(self):
		self.empid = int(input("Enter empid "))
		self.name = input("Enter name ")
		self.designation = input("Enter designation ")
		self.salary = int(input("Enter salary "))
#		self.project_ids = set(input("Enter project ids"))
#		self.skills = 
	def display_projectids(self):
#		print(self.project_ids)
		print("Project ids ")
	def display_identity(self):
		print(self.empid)
	def check_relevant_skills(self):
#		print(self.skills)
		print("Skils")
	@classmethod
	def display_company_details(cls):
		print(cls.cname)
e1 = employee()
e1.display_projectids()
e1.display_identity()
e1.check_relevant_skills()
e1.display_company_details()
