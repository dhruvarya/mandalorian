from node import Node
from slant_obstacle import Slant_obstacle
from vector import Vector
import random
from shapes import *
import select
import sys
import termios
import time
import tty

class Screen():
    """ class to represent the scene of game """
    def __init__(self):
        self.__screen = []
        for i in range(49):
            temp = []
            for j in range(174):
                temp.append(" ")
            temp.append("\n")
            self.__screen.append(temp)
        self.__SPEED = 0.1
        self.__obstacles = []
        self.__coins = []
        self.__magnets = []
        self.__bullets = []
        self.__b_bullets = []
        self.__powerups = []
        self.__powerup_time = -1

    def getChar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        time.sleep(self.__SPEED)

        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return sys.stdin.read(1)

        else:
            return ""


    def __str__(self):
        s = ""
        for i in range(49):
            for j in range(174):
                s += self.__screen[i][j]
            s += "\n"
        return s

    def place(self, Node):
        for i in range(Node.getcbox().x):
            for j in range(Node.getcbox().y):
                if Node.getpos().x + i >= 0 and Node.getpos().y + j >= 0 and Node.getpos().x + i <= 173 and Node.getpos().y + j <= 173:
                    self.__screen[Node.getpos().x + i][Node.getpos().y + j] = Node.getshape(i, j)

    def clear(self):
        self.__screen = []
        for i in range(49):
            temp = []
            for j in range(174):
                temp.append(" ")
            self.__screen.append(temp)


    def generate_coins(self):
        vx = random.randint(6, 42)
        for i in range(4):
            for j in range(4):
                self.__coins.append(Node(coin_shape(), Vector(vx + i, 166 + j)))

    def generate_magnet(self):
        self.__magnets.append(Node(magnet_shape(), Vector(random.randint(6, 38), random.randint(1, 166))))

    def delete_magnet(self):
        self.__magnets = []

    def generate_obstacles(self, shape):
        self.__obstacles.append(Node(shape, Vector(random.randint(6, 38), 166)))

    def generate_slant_obstacle(self, shape):
        self.__obstacles.append(Slant_obstacle(shape, Vector(random.randint(6, 38), 166)))

    def generate_bullets(self, pos):
        self.__bullets.append(Node(gun_shape(), pos))

    def generate_b_bullets(self, pos):
        self.__b_bullets.append(Node(gun_l_shape(), pos))

    def generate_powerup(self):
        self.__powerups.append(Node(powerup_shape(), Vector(random.randint(6, 38), 166)))

    def move_obstacles(self, user):
        for magnet in self.__magnets:
            self.place(magnet)
            user.attract(magnet)

        for bullet in self.__bullets:
            self.place(bullet)
            bullet.move(Vector(0, 2))


        for coin in self.__coins:
            self.place(coin)
            coin.move(Vector(0, -1))
            if coin.isCollide(user):
                user.increment_score()
                self.__coins.remove(coin)

        for obstacle in self.__obstacles:
            self.place(obstacle)
            obstacle.move(Vector(0, -1))
            for bullet in self.__bullets:
                if obstacle.isCollide(bullet):
                    self.__obstacles.remove(obstacle)
                    self.__bullets.remove(bullet)
            if obstacle.isCollide(user):
                user.decrement_lives()
                self.__obstacles.remove(obstacle)

        for powerup in self.__powerups:
            self.place(powerup)
            powerup.move(Vector(0, -1))
            if powerup.isCollide(user):
                self.__SPEED = 0.05
                self.__powerups.remove(powerup)
                self.__powerup_time = 150

        self.__powerup_time -= 1
        if self.__powerup_time == 0:
            self.__SPEED = 0.1

    def check_collision(self, user,  boss):
        for bullet in self.__bullets:
            if bullet.isCollide(boss):
                self.__bullets.remove(bullet)
                boss.decrement_lives()

        for b_bullet in self.__b_bullets:
            self.place(b_bullet)
            b_bullet.move(Vector(0, -2))
            if b_bullet.isCollide(user):
                self.__b_bullets.remove(b_bullet)
                user.decrement_lives()

                



