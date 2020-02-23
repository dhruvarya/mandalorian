import os
from colorama import Fore, Back
import math
import random
from screen import Screen
from node import Node
from counters import Counter
from vector import Vector
from mandalorian import Mandalorian
from slant_obstacle import Slant_obstacle
from shapes import *

t = 1600

user = Mandalorian(player_shape(), Vector(41, 0))
boss = Mandalorian(dragon_shape(), Vector(30, 120))
ground1 = Node(gg1_shape(), Vector(44, 0))
ground2 = Node(gg2_shape(), Vector(1, 0))
ground2_down = Node(gg2_down_shape(), Vector(5, 0))
game_over = Node(game_over(), Vector(9, 0))
scorer = Counter(score_shape(), Vector(2, 156))
liver = Counter(lives_shape(), Vector(3, 156))
timer = Counter(timer_shape(), Vector(4, 156))

sc = Screen()

gravity = Vector(1, 0)
thrust = Vector(-2, 0)
gun_speed = Vector(0, 1)

while t > 0:
    os.system('clear')
    print(sc)
    print("user health: " + str(user.lives_remaining()) + " boss health: " + str(boss.lives_remaining()), end = '')
    if user.shield_available():
        print(" Shield is available")
    elif user.getshieldtimer() < 200:
        print(" Shield left for ", (200 - user.getshieldtimer())/10)
    else:
        print(" Shield will be activated in ", (800 - user.getshieldtimer())/10)
    if user.lives_remaining() <= 0 or boss.lives_remaining() <= 0:
        break

    sc.clear()
    ch = sc.getChar()
    thrust = Vector(0, 0)
    
    if ch == 'a':
        user.move(Vector(0, -2))
    elif ch == 'w':
        thrust = Vector(-2, 0)
    elif ch == 'd':
        user.move(Vector(0, 2))
    elif ch == 'f':
        sc.generate_bullets(user.position())
    elif ch == ' ':
        if user.shield_available():
            user.activate_shield()
    elif ch == 'q':
        exit()

    user.apply(gravity + thrust)
    
    if t > 400:
        if t%125 == 0:
            sc.generate_coins()

        if t%125 == 50:
            sc.generate_slant_obstacle(slant_obstacle_shape())

        if t%125 == 25:
            sc.generate_obstacles(hlines_shape())

        if t%125 == 75:
            sc.generate_obstacles(vlines_shape())

        if t%125 == 100:
            sc.generate_powerup()

        if t%400 == 300:
            sc.generate_magnet()

        if t%400 == 200:
            sc.delete_magnet()

    else:
        sc.place(boss)
        boss.bossmove(user.position())
        sc.check_collision(user, boss)
        if t % 15 == 0:
            sc.generate_b_bullets(boss.position())
            sc.generate_b_bullets(boss.position() + Vector(2, 0))
            sc.generate_b_bullets(boss.position() + Vector(4, 0))
        if t % 15 == 4:    
            sc.generate_b_bullets(boss.position() + Vector(6, 0))
            sc.generate_b_bullets(boss.position() + Vector(8, 0))
            sc.generate_b_bullets(boss.position() + Vector(10, 0))
        if t % 15 == 8:    
            sc.generate_b_bullets(boss.position() + Vector(12, 0))
            sc.generate_b_bullets(boss.position() + Vector(14, 0))

    sc.move_obstacles(user)

    liver.update(user.lives_remaining())
    timer.update(math.floor(t/10))
    scorer.update(user.current_score())
    sc.place(ground1)
    sc.place(ground2)
    sc.place(ground2_down)
    sc.place(scorer)
    sc.place(timer)
    sc.place(liver)
    sc.place(user)
    t -= 1
    user.increment_shield_timer()

sc.clear()
sc.place(ground2)
sc.place(ground1)
sc.place(ground2_down)
sc.place(game_over)
print(sc)

if user.lives_remaining() == 0:
    print("You could not save baby yoda.")

elif boss.lives_remaining() == 0:
    print("Congratulations! You saved baby yoda.") 

else:
    print("Time's up!")