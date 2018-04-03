class Animal():

	def __init__(self):
		print('Animal Created')

	def who_am_i(self):
		print('I am an animal')

	def eat(self):
		print('I am eating')

class Dog(Animal):
	'''
	Animals and Dogs have overlapping attributes, so I want 
	Dog to inherit from the Animal class 
	'''
	def __init__(self):
		Animal.__init__(self)
		print('Dog Created')

	#If I want to overwrite an animal attirbute Dog inherrited, overwrite it
	def who_am_i(self):
		print('I am a dog')

	#Can write new methods only for Dog that Animals don't use
	def bark(self):
		print('Woof!')

