# method overriding example

class college:
	def __init__(self,name,capacity):
		self.name = capacity
		self.capacity = capacity
	def display(self):
		print("In college class ")
		print(self.name, self.capacity)

class mba_college(college):
	def __init__(self,name,capacity,placement):
		college.__init__(self,name,capacity)
		#super.__init__(name,capacity)
		self.placement = placement
	def display(self):
		print("In mba class")
		print(self.name, self.capacity,self.placement)

c1 = college("ABC",120)
c1.display()
mba1 = mba_college("XYZ",120,100)
mba1.display()
