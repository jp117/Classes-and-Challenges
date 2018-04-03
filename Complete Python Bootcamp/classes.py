class Dog():
	#Classes are CamelCase

	#class object attribute
	#same for any instance of a class
	species = 'mammal'


	def __init__(self,breed, name, spots):

		# Attributes
		#We take in the argument and assign it
		self.breed = breed
		self.name = name

		#expect boolean True/False
		self.spots = spots

	#Operations/Actions ----> Methods
	def bark(self):
		print('WOOF')

class Circle():

	#Class object attribute
	pi = 3.14

	def __init__(self, radius=1):

		self.radius = radius
		self.area = radius*radius*Circle.pi

	#method
	def get_circumference(self):
		return self.radius*self.pi*2