from vector import Vector

class Node(object):

    def __init__(self, shape, pos):
        self._shape = shape
        self._pos = pos
        self._vel = Vector(0, 0)
        self._cbox = Vector(len(shape), len(shape[0]))

    def setshape(self, x, y, val):
        self._shape[x][y] = val

    def getshape(self, x, y):
        return self._shape[x][y]

    def move(self, force):
        self._pos = self._pos + force
        if self._pos.x == 0:
            self._shape = []
            self._cbox = Vector(0,0)
        if self._pos.y == 175:
            self._shape = []
            self._cbox = Vector(0,0)

    def getpos(self):
        return self._pos

    def getcbox(self):
        return self._cbox

    def isCollide(self, other):
        if self._pos.x + self._cbox.x < other.getpos().x:
            return False

        if self._pos.x > other.getpos().x + other.getcbox().x:
            return False

        if self._pos.y + self._cbox.y < other.getpos().y:
            return False

        if self._pos.y > other.getpos().y + other.getcbox().y:
            return False

        return True
