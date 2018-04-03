class Animal():

	def __init__(self,name):
		self.name = name

	def speak(self):
		'''
		We don't want this to be called, we want the other animal 
		classes that share attributes to implement it
		'''
		raise NotImplementedError('Subclass must impolement this abstract method')

class Dog(Animal):

	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + ' says woof!'

class Cat(Animal):

	def __init__(self, name):
		self.name = name

	def speak(self):
		return self.name + ' says meow!'

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

'''
Even though niko and felix are both calling speak, they are
calling a different speak.  That's polymorphism.
'''