
class cooler:
	def __init__(self):
		self.brand = input("Enter brand ")
		self.airflow_capacity = 60
		self.swing = True
	def __str__(self):
		# returns string representation of the object
		return "Brand = "+self.brand +\
			 " Airflow capacity = "+str(self.airflow_capacity) + " swing = "+ str(self.swing)

c1 = cooler()
print(c1) # this calls __str__ method for c1
