# import

import time
import pygame
import sys
import random

# -----------------------------------------------------------------------------------------------------------------------
# color

red = (240, 40, 40)
green = (0, 220, 0)
blue = (30, 144, 255)
# darkBlue = (0,0,128)
white = (255, 255, 255)
black = (15, 15, 15)
pink = (255, 180, 180)
yellow = (238, 238, 0)
orange = (255, 150, 0)
purple = (138, 43, 226)
brown = (139, 76, 57)

colors = [red, green, blue, white, pink, yellow, orange, purple, brown]

base_color = colors[random.randint(0, 8)]
tower_color = colors[random.randint(0, 8)]
disk_color = colors[random.randint(0, 8)]

# -----------------------------------------------------------------------------------------------------------------------
# variables

n = int(input("Number of discs: "))
wait = float(input("Delay in seconds (or 0 for no delay and -1 for auto calculation): "))
if wait==-1: wait = min(max(10 / 2 ** n - .02, 0), 2)
tower_x = (155, 320, 485)
tower_y = 440
tower_height = 400
disk_thickness = 15
discn_width = 150
tower_width = 10
base_width = 600
base_height = 20
base_x = 320


# -----------------------------------------------------------------------------------------------------------------------


def draw_towers():
    screen.fill((black))

    pygame.draw.rect(screen, (base_color), ((screen_coord[0] - base_width) / 2, tower_y, base_width, base_height), 0)

    pygame.draw.rect(screen, (tower_color),
                     (tower_x[0] - tower_width / 2, tower_y - tower_height, tower_width, tower_height), 0)
    pygame.draw.rect(screen, (tower_color),
                     (tower_x[1] - tower_width / 2, tower_y - tower_height, tower_width, tower_height), 0)
    pygame.draw.rect(screen, (tower_color),
                     (tower_x[2] - tower_width / 2, tower_y - tower_height, tower_width, tower_height), 0)

    pygame.display.update()


# ------------------------------------------------------------------------


def draw_one_disk(disk, pos, tower):
    xfunc = (discn_width - (n - disk) * (discn_width / n)) / 2
    widthfunc = discn_width - (n - disk) * (discn_width / n)
    pygame.draw.rect(screen, (disk_color), (
    (tower_x[tower]) - xfunc, tower_y - disk_thickness - pos * disk_thickness, widthfunc, disk_thickness), 0)
    pygame.display.update()


# ------------------------------------------------------------------------


def draw_stacks():
    for i in range(1, len(tower1)):
        draw_one_disk(tower1[i], i - 1, 0)

    for i in range(1, len(tower2)):
        draw_one_disk(tower2[i], i - 1, 1)

    for i in range(1, len(tower3)):
        draw_one_disk(tower3[i], i - 1, 2)

    time.sleep(wait)


# ------------------------------------------------------------------------

def move_disks_1(s, e):
    s.remove(1)
    e.append(1)
    # print("tower 1:{0:30s} tower 2:{1:30s} tower 3:{2:30s}".format(str(tower1[1:]), str(tower2[1:]), str(tower3[1:])))
    draw_towers()
    draw_stacks()


# ------------------------------------------------------------------------


def move_disks(s, e, N):
    pygame.event.get()
    if N == 1:
        move_disks_1(s, e)
    else:
        if s == tower1:
            if e == tower3:
                mid = tower2
            else:
                mid = tower3

        if s == tower2:
            if e == tower3:
                mid = tower1
            else:
                mid = tower3

        if s == tower3:
            if e == tower1:
                mid = tower2
            else:
                mid = tower1

        move_disks(s, mid, N - 1)

        s.remove(N)
        e.append(N)
        draw_towers()

        draw_stacks()

        move_disks(mid, e, N - 1)


screen_coord = (640, 480)
screen = pygame.display.set_mode(screen_coord)

draw_towers()
time.sleep(.5)

tower1 = ['a']
tower2 = ['b']
tower3 = ['c']
tmp = []
for i in range(1, n + 1):
    tmp.append(i)
tmp.reverse()
tower1[1:] = tmp

draw_stacks()
move_disks(tower1, tower3, n)

time.sleep(1)
