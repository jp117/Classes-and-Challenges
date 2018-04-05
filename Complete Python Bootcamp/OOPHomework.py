class Line:

	def __init__(self, coor1, coor2):

		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):

		return ((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)**.5

	def slope(self):

		return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
#expected output is 9.4339 if input properly

print(li.slope())
#expected output is 1.6 if input properly

class Cylinder:

	pi = 3.14

	def __init__(self,height=1, radius=1):
		
		self.height = height
		self.radius = radius
		

	def volume(self):

		return self.pi*self.radius**2*self.height

	def surface_area(self):

		return 2*self.pi*self.radius*self.height + 2* self.pi * self.radius**2

c = Cylinder(2,3)

print(c.volume())
#expected output of volume is 56.52 if everything implemented properly

print(c.surface_area())
#Expected output is 94.2 if everything input properly.