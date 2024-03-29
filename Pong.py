
import random
import pygame
import time
import math
from timeit import default_timer as timer
import sys

global mode
screen_coord = (800, 600) # 800, 600
screen = pygame.display.set_mode(screen_coord)
pygame.init()
font = pygame.font.SysFont("comicsansms", 20) # 21
lscore, rscore, totalhits = 0, 0, 0

paddleheight = 100 #100
paddlewidth = 20 #20

black = (20, 20, 20)
red = (240, 40, 40)
green = (0, 220, 0)
blue = (30, 144, 255)
white = (250, 250, 250)
pink = (255, 180, 180)
yellow = (238, 238, 0)
orange = (255, 150, 0)
purple = (138, 43, 226)
brown = (139, 76, 57)

colors = [red, green, blue, white, pink, yellow, orange, purple, brown]

def instructions():
    global mode
    print('\nNOTE:\nIf you see a pygame message but no window, you may have to find the window on your computer.')
    ins = ['Welcome to Pahan\'s Python Ping-Pong Game! ',
           'Left Paddle: W/S keys, Right Paddle: Up/Down arrows',
           'You can see scores and total hits in the ongoing point at the top.',
           'Press space to reset the score and R to come back to this menu.',
           'human (right) vs computer (left): e=easy, m=medium, h=hard, a=AI',
           'p: human vs human, s: AI showdown',
           'Press the corresponding key from above to play!']
    for i in range(0, len(ins)):
        text = font.render(ins[i], True, white)
        screen.blit(text, (50, 100 + 30 * i))
        pygame.display.update()

    while True:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            mode = 'p'
            break
        if keys[pygame.K_e]:
            mode = 'e'
            break
        if keys[pygame.K_m]:
            mode = 'm'
            break
        if keys[pygame.K_h]:
            mode = 'h'
            break
        if keys[pygame.K_a]:
            mode = 'a'
            break
        if keys[pygame.K_s]:
            mode = 's'
            break
        if keys[pygame.K_f]:
            mode = 'f'
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()


def printscore(totalhits, lscore, rscore, x, y, scoredist):
    text = font.render('Score:', True, white)
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2 - scoredist))
    screen.blit(text, (screen_coord[0] - x - text.get_width() // 2, y - text.get_height() // 2 - scoredist))

    text = font.render(str(lscore), True, white)
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    text = font.render(str(rscore), True, white)
    screen.blit(text, (screen_coord[0] - x - text.get_width() // 2, y - text.get_height() // 2))

    text = font.render('Total hits:', True, white)
    screen.blit(text, (screen_coord[0] // 2 - text.get_width() // 2, y - text.get_height() // 2 - scoredist))

    text = font.render(str(totalhits), True, white)
    screen.blit(text, (screen_coord[0] // 2 - text.get_width() // 2, y - text.get_height() // 2))


def three21():
    for i in [3,2,1]:
        screen.fill(black)
        bigfont = pygame.font.SysFont("comicsansms", 100)
        text=bigfont.render(str(i), True, (250,250,250))
        screen.blit(text,((screen_coord[0]-text.get_width())//2,(screen_coord[1]-text.get_height())//2))
        pygame.display.update()
        time.sleep(1)


class Ball:

    def __init__(self):
        self.x = screen_coord[0] / 2
        self.y = screen_coord[1] / 2
        self.radius = 13 # 13
        self.color = random.choice(colors)
        self.dirchange = 5 # 5
        self.sidedirchange = 60 # 60
        self.defaultSpeed = {'e':200,'m':250,'h':300,'a':350,'p':250,'s':350,'f':350}[mode] # pixels per sec
        self.speed = self.defaultSpeed
        self.speedIncrease = 15 # 15
        if random.random() < .5:
            self.dir = random.randint(-self.sidedirchange, self.sidedirchange)
        else:
            self.dir = random.randint(180 - self.sidedirchange, 180 + self.sidedirchange)

    def draw(self):
        pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius, 0)

    # Calculate the point the ball will be in the next frame
    def updatePoint(self, updateSpeed):
        newx = self.x + (self.speed * math.cos(math.radians(self.dir)) / updateSpeed)
        newy = self.y + (self.speed * math.sin(math.radians(self.dir)) / updateSpeed)
        return newx, newy

    # Check if the ball should be reflected the next frame
    def invalid(self, newx, newy, leftPaddle, rightPaddle):

        if newy + self.radius >= screen_coord[1]:
            return 'bottomWall'

        if newy <= self.radius:
            return 'topWall'

        rpaddlecontacty = newy - (math.sin(math.radians(self.dir)) * (newx - screen_coord[0] + rightPaddle.width))
        if newx + self.radius > rightPaddle.x and rightPaddle.y - 15 <= rpaddlecontacty <= \
                rightPaddle.y + rightPaddle.height + 15:
            return 'rightPaddle'

        lpaddlecontacty = newy - (math.sin(math.radians(self.dir)) * (leftPaddle.width - newx))
        if newx - self.radius < leftPaddle.width and leftPaddle.y - 15 <= lpaddlecontacty <= \
                leftPaddle.y + leftPaddle.height + 15:
            return 'leftPaddle'

        return 'valid'

    #Reflect the ball off a given object
    def reflect(self, newx, newy, object, leftPaddle, rightPaddle):
        global totalhits
        newdir = self.dir

        if object == 'rightPaddle':
            newx = newx - 2 * ((newx + self.radius) - rightPaddle.x)
            # newy = self.y
            newdir = 180 - (self.dir - 0) + random.randint(-self.dirchange, self.dirchange)
            totalhits += 1
            self.speed += self.speedIncrease

        if object == 'leftPaddle':
            newx = newx + 2 * (leftPaddle.width - (newx - self.radius))
            # newy = self.y
            newdir = 0 - (self.dir - 180) + random.randint(-self.dirchange, self.dirchange)
            totalhits += 1
            self.speed += self.speedIncrease

        if object == 'bottomWall':
            # newx = self.x
            newy = newy - 2 * ((newy + self.radius)-screen_coord[1])
            newdir = 270 - (self.dir - 90) + random.randint(-self.dirchange, self.dirchange)

        if object == 'topWall':
            # newx = self.x
            newy = newy + 2 * (0-(newy-self.radius))
            newdir = 90 - (self.dir - 270) + random.randint(-self.dirchange, self.dirchange)

        return newx, newy, newdir

    #Update the ball for the next frame
    def updateBall(self, updateSpeed, leftPaddle, rightPaddle, reset):
        global rscore
        global lscore
        global totalhits
        newx, newy = self.updatePoint(updateSpeed)
        v = self.invalid(newx, newy, leftPaddle, rightPaddle)
        newx, newy, newdir = self.reflect(newx, newy, v, leftPaddle, rightPaddle)

        self.x, self.y, self.dir = newx, newy, newdir
        if self.x < 0 and v!='leftpaddle' or self.x > screen_coord[0] and v!='rightpaddle' or reset:
            three21()
            leftPaddle.y=screen_coord[1] / 2 - paddleheight / 2
            rightPaddle.y=screen_coord[1] / 2 - paddleheight / 2
            if self.x < 0:
                rscore += 1
            if self.x > screen_coord[0]:
                lscore += 1
            self.speed = self.defaultSpeed
            self.x = screen_coord[0] / 2
            self.y = screen_coord[1] / 2
            side = random.randint(1, 2)
            if side == 1:
                self.dir = random.randint(-self.sidedirchange, self.sidedirchange)
            else:
                self.dir = random.randint(180 - self.sidedirchange, 180 + self.sidedirchange)
            # print('Total hits:',totalhits)
            totalhits = 0

        self.speed = self.speed + self.speedIncrease / updateSpeed
        self.draw()
        if 90-self.dirchange-5 < (self.dir % 180) < 90:
            self.dir -= 10
        if 90+self.dirchange+5 > (self.dir % 180) > 90:
            self.dir += 10


# ===========================================
class Paddle:

    # set the paddle up
    def __init__(self, x, upkey, downkey):
        self.upkey = upkey
        self.downkey = downkey
        self.x = x
        self.y = screen_coord[1] / 2 - paddleheight / 2
        self.height = paddleheight
        self.width = paddlewidth
        self.color = random.choice(colors)
        self.speed = 800 # 600
        if mode == 'f': self.speed=10000

    def spot(self):
        dir = ball.dir % 360

        if 90 < dir < 270:
            if self.upkey == 'w':
                xchange = ball.x - (self.x + self.width)
            else:
                xchange = screen_coord[0] + ball.x - 3 * self.width
        else:
            if self.upkey == 'w':
                xchange = -(2 * screen_coord[0] - 3 * self.width - ball.x)
            else:
                xchange = self.x - ball.x

        if self.upkey == 'w' or 90 < dir < 270:
            now = -(math.tan(math.radians(dir))) * xchange + ball.y
        else:
            now = (math.tan(math.radians(dir))) * xchange + ball.y

        while now > screen_coord[1] or now < 0:
            if now < 0:
                now = -now
            else:
                now = 2 * screen_coord[1] - now

        return now

    # draw the paddle
    def draw(self):
        pygame.draw.rect(screen, self.color, (round(self.x), round(self.y), self.width, self.height))

    # check input, change coordinates, and draw
    def keyspressed(self):
        global mode
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if self.downkey == 'downarrow':
            # downkey = keys[pygame.K_DOWN]
            if mode in ['p', 'h', 'm', 'e', 'a']:
                downkey = keys[pygame.K_DOWN]
            if mode in 'sf':
                if self.spot() > self.y + self.height / 2:
                    downkey = 1
                else:
                    downkey = 0
        if self.upkey == 'uparrow':
            # upkey = keys[pygame.K_UP]
            if mode in ['p', 'h', 'm', 'e', 'a']:
                upkey = keys[pygame.K_UP]
            if mode in 'sf':
                if self.spot() < self.y + self.height / 2:
                    upkey = 1
                else:
                    upkey = 0
        if self.downkey == 's':
            if mode in ['p']:
                downkey = keys[pygame.K_s]
            if mode in ['s', 'a', 'f']:
                downkey = self.spot() > self.y + self.height / 2
            if mode in ['h']:
                downkey = ball.y > self.y + self.height / 2
            if mode in ['e']:
                downkey = ball.y > self.y + self.height / 2 and random.randint(1, 4) == 1
            if mode in ['m']:
                downkey = ball.y > self.y + self.height / 2 and random.randint(1, 2) == 1
        if self.upkey == 'w':
            if mode in ['p']:
                upkey = keys[pygame.K_w]
            if mode in ['s', 'a', 'f']:
                upkey = self.spot() < self.y + self.height / 2
            if mode in ['h']:
                upkey = ball.y < self.y + self.height / 2
            if mode in ['e']:
                upkey = ball.y < self.y + self.height / 2 and random.randint(1, 4) == 1
            if mode in ['m']:
                upkey = ball.y < self.y + self.height / 2 and random.randint(1, 2) == 1

        if downkey == True and upkey == False:
            return 'down'
        if downkey == False and upkey == True:
            return 'up'
        if downkey == True and upkey == True:
            return 'both'
        if downkey == False and upkey == False:
            return 'none'

    def updatePaddle(self):
        if self.keyspressed() == 'down' and self.y <= screen_coord[1] - self.height:
            self.y = self.y + self.speed / updateSpeed
        if self.keyspressed() == 'up' and self.y >= 0:
            self.y = self.y - self.speed / updateSpeed
        self.draw()


instructions()
ball = Ball()
leftPaddle = Paddle(0, 'w', 's')
rightPaddle = Paddle(screen_coord[0] - paddlewidth, 'uparrow', 'downarrow')
prevtime, resettime, reset = 0, 0, 0
three21()

while True:
    curtime = timer()
    # time.sleep(max(0,1 / updateSpeed + prevtime - curtime))
    if curtime - prevtime < .5: updateSpeed=1/(curtime - prevtime)
    prevtime = timer()

    screen.fill(black)
    leftPaddle.updatePaddle()
    rightPaddle.updatePaddle()
    ball.updateBall(updateSpeed, leftPaddle, rightPaddle, reset)
    printscore(totalhits, lscore, rscore, 50, 50, 20)
    pygame.display.update()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        lscore, rscore, totalhits = 0, 0, 0
        reset = True
    else: reset = False

    if pygame.key.get_pressed()[pygame.K_r]:
        screen.fill(black)
        instructions()
        ball = Ball()
        leftPaddle = Paddle(0, 'w', 's')
        rightPaddle = Paddle(screen_coord[0] - paddlewidth, 'uparrow', 'downarrow')
        prevtime, resettime, lscore, rscore, reset = 0, 0, 0, 0, 0
        three21()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
