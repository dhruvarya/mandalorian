import math
from node import Node

class Counter(Node):

	def update(self, val):
		self._shape[0][-1] = str(val%10)
		val = math.floor(val/10)
		self._shape[0][-2] = str(val%10)
		val = math.floor(val/10)
		self._shape[0][-3] = str(val%10)



