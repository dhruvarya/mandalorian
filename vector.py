class Vector(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"