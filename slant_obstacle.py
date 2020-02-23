from node import Node
from vector import Vector

class Slant_obstacle(Node):

	def isCollide(self, other):
		for i in range(8):
			box = Node([["o", "o"]], self._pos + Vector(i, i))
			if box.isCollide(other):
				return True
		return False