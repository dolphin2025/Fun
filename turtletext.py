import turtle as t
import time

letters = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!-'
simcode = [[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1],
           [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0],
           [1, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1],
           [1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1],
           [1, 0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0],
           [1, 1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1],
           [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0],
           [1, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1],
           [1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1],
           [1, 0, 1, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 0, 0, 1],
           [1, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1]]


def pen(l, n):
    if simcode[letters.index(l)][n - 1] == 1:
        t.pd()
    else:
        t.pu()


def turtletext(text, speed=1, size=2):
    t.width(2 * size)
    m = 5 * size
    t.pu()
    t.speed(speed)
    t.left(180)
    t.forward(350 + 4 * size)
    t.left(180)
    for l in text:
        if l == 't' or l == 'T':
            t.pu()
            t.forward(m)
            t.pd()
            t.pencolor('green')
            t.right(90)
            t.circle(m / 2)
            # t.left(90)
            t.pu()
            t.right(135)
            # t.forward(m/10)
            t.pd()
            t.width(size)
            t.forward(m / 2)
            t.left(180)
            t.forward(m / 2)
            t.right(90)
            t.forward(m / 2)
            t.pu()
            t.right(180)
            t.forward(m / 2)
            t.right(45)
            t.forward(m * 1.2)
            t.pd()
            t.right(90)
            t.circle(m / 5)
            t.pu()
            t.right(90)
            t.forward(m / 1.5)
            t.left(90)
            t.forward(m / 2)
            t.pd()
            t.forward(m / 2)
            t.left(180)
            t.pu()
            t.forward(1.5 * m)
            t.pd()
            t.forward(m / 2)
            t.left(180)
            t.pu()
            t.forward(m)
            t.left(90)
            t.forward(m / 1.5)
            t.width(2 * size)
            t.color('black')

        else:
            t.pu()
            t.forward(m)
            t.left(90)
            if simcode[letters.index(l)][1 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            t.right(90)

            if simcode[letters.index(l)][2 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            t.right(90)
            if simcode[letters.index(l)][3 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            t.right(0)
            if simcode[letters.index(l)][4 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            if l in '.,!':
                t.width(size)
                t.dot()
                t.width(2 * size)
            t.right(90)
            if simcode[letters.index(l)][5 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            t.right(90)
            if simcode[letters.index(l)][6 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
            t.right(90)
            if simcode[letters.index(l)][7 - 1] == 1:
                t.pd()
            else:
                t.pu()
            t.forward(m)
    t.ht()
    time.sleep(5)


turtletext(input('Enter the text you would like turtletext to print: ').upper())
