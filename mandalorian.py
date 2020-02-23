from node import Node
from vector import Vector
from colorama import Fore

class Mandalorian(Node):

    def __init__(self, shape, pos):
        self._shape = shape
        self._pos = pos
        self._vel = Vector(0, 0)
        self._cbox = Vector(len(shape), len(shape[0]))
        self.__lives = 20
        self.__score = 0
        self.__shield_activated = False
        self.__shield_timer = 201

    def increment_score(self):
        self.__score += 1

    def increment_shield_timer(self):
        self.__shield_timer += 1
        if self.__shield_timer == 200:
            self.deactivate_shield()
        if self.__shield_timer >= 800:
            self.prompt_shield()

    def decrement_lives(self):
        if not self.__shield_activated:
            self.__lives -= 1

    def position(self):
        return self._pos

    def current_score(self):
        return self.__score

    def lives_remaining(self):
        return self.__lives

    def move(self, force):
        self._pos = self._pos + force
        
        if self._pos.x <= 6:
            self._pos.x = 6
            self._vel.x = 0
        
        if self._pos.x > 41:
            self._pos.x = 41
            self._vel.x = 0
        
        if self._pos.y < 0:
            self._pos.y = 0
        
        if self._vel.x > 3:
            self._vel.x = 3
        
        if self._vel.x < 0:
            self._shape[1][0] = Fore.WHITE + "\\"
            self._shape[1][2] = "/"
        else:
            self._shape[1][0] = Fore.WHITE + "/"
            self._shape[1][2] = "\\"

    def apply(self, force):
        self._vel = self._vel + force
        self._pos = self._pos + self._vel
        
        if self._pos.x <= 6:
            self._pos.x = 6
            self._vel.x = 0
        
        if self._pos.x > 41:
            self._pos.x = 41
            self._vel.x = 0
        
        if self._pos.y < 0:
            self._pos.y = 0
        
        if self._vel.x > 2:
            self._vel.x = 2

        if self._vel.y > 2:
            self._vel.y = 2
        
        if self._vel.x < 0:
            self._shape[1][0] = Fore.WHITE + "\\"
            self._shape[1][2] = "/"
        else:
            self._shape[1][0] = Fore.WHITE + "/"
            self._shape[1][2] = "\\"

    def attract(self, magnet):
        if self._pos.y > magnet.getpos().y:
            self.move(Vector(0, -1))

        elif self._pos.y < magnet.getpos().y:
            self.move(Vector(0, 1))

        if self._pos.x > magnet.getpos().x:
            self.move(Vector(-4, 0))

        elif self._pos.x < magnet.getpos().x:
            self.move(Vector(4, 0))

    def shield_available(self):
        if self.__shield_timer >= 800:
            return True
        else:
            return False

    def getshieldtimer(self):
        return self.__shield_timer

    def activate_shield(self):
        self.__shield_activated = True
        self._shape = [[Fore.WHITE + "S", "@", "S"], [ Fore.WHITE + "/", "|", "\\"], [Fore.WHITE + "S", " ", "S"]]
        self.__shield_timer = 0

    def deactivate_shield(self):
        self.__shield_activated = False
        self._shape = [[Fore.WHITE + "<", "@", ">"], [ Fore.WHITE + "/", "|", "\\"], [Fore.WHITE + "/", " ", "\\"]]

    def prompt_shield(self):
        self._shape = [[Fore.WHITE + "<", "@", ">"], [ Fore.WHITE + "/", "S", "\\"], [Fore.WHITE + "/", " ", "\\"]]

    def bossmove(self, pos):
        if self._pos.x > pos.x and self._pos.x > 0:
            self._pos.x -= 1

        if self._pos.x < pos.x and self._pos.x < 30:
            self._pos.x += 1