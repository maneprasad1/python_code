
class mmart:
	def __init__(self):
		self.items = ['rice','wheat','veggies','chips']
		self.owner = "Mallya"
		self.area = '3000 sqft'
		self.location = 'Pune'
	def displayitems(self):
		print("Items in mmart")
		for i in self.items:
			print(i)
	def displaydetails(self):
		print("Owner",self.owner, "Area",self.area,"Location", self.location)

m1 = mmart()
m1.displayitems()
m1.displaydetails()
