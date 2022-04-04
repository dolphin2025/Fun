import random
import pygame
import time
import math

sc = (800, 600)
screen = pygame.display.set_mode(sc)
size = 200  # 200
border = 20  # 20
tsize = 35  # 35
pygame.init()
font = pygame.font.SysFont("comicsansms", 20)

black = (20, 20, 20)
white = (250, 250, 250)


def ctuple(board):
    return ((board[0][0], board[0][1], board[0][2]), (board[1][0], board[1][1], board[1][2]),
            (board[2][0], board[2][1], board[2][2]))


def clist(board):
    return [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]]]


def instructions(font):
    print()
    print('NOTE:')
    print('If you see a pygame message but no window, you may have to find the window on your computer.')
    dist = 25
    ins = ['Welcome to Pahan\'s Python Tic-Tac-Toe Game! ',
           'p = player vs player, c = player vs computer',
           'Press the corresponding key from above to continue!']
    for i in range(0, len(ins)):
        text = font.render(ins[i], True, (250, 250, 250))
        screen.blit(text, (50, 100 + dist * i))
        pygame.display.update()
    while True:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            mode = 'p'
            break
        if keys[pygame.K_c]:
            mode = 'c'
            break
    cf = True
    if mode == 'c':
        pygame.draw.rect(screen, black, (0, 0, sc[0], sc[1]))
        ins = ['Do you really think you can beat me?',
            '1=you first, 2=me first',
               'Press the corresponding key from above to play!']
        for i in range(0, len(ins)):
            text = font.render(ins[i], True, (250, 250, 250))
            screen.blit(text, (50, 100 + dist * i))
            pygame.display.update()
        while True:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                cf = False
                break
            if keys[pygame.K_2]:
                cf = True
                break
    return mode, cf


def drawboard(board, size, border):
    pygame.draw.rect(screen, black, (0, 0, sc[0], sc[1]))
    text = 'Click the square you would like to place on.'
    screen.blit(font.render(text, True, (250, 250, 250)), (215, 45))
    pygame.display.update()
    pygame.draw.rect(screen, white, (sc[0] // 2 - size, sc[1] // 2 - size, 2 * size, 2 * size))
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            pygame.draw.rect(screen, black,
                             (sc[0] / 2 - size + border + (i - 1) * (2 * (size - 2 * border) / 3 + border),
                              border + sc[1] / 2 - size + (j - 1) * (2 * (size - 2 * border) / 3 + border),
                              2 * (size - 2 * border) / 3, 2 * (size - 2 * border) / 3))
            x_o = board[j - 1][i - 1]
            centerx = int(sc[0] / 2 - size + border + (i - 1) * (2 * (size - 2 * border) / 3 + border) + 2 * (
                        size - 2 * border) / 6)
            centery = int(border + sc[1] / 2 - size + (j - 1) * (2 * (size - 2 * border) / 3 + border) + 2 * (
                        size - 2 * border) / 6)
            if x_o == 2:
                pygame.draw.circle(screen, white, (centerx, centery), tsize, 0)
                pygame.draw.circle(screen, black, (centerx, centery), tsize - border // 2, 0)
            elif x_o == 1:
                xsize = 7
                cdist = int(math.sqrt(2) * xsize)
                startx = int(sc[0] / 2 - size + border + (i - 1) * (2 * (size - 2 * border) / 3 + border) + 2 * (
                            size - 2 * border) / 6) - tsize
                starty = int(border + sc[1] / 2 - size + (j - 1) * (2 * (size - 2 * border) / 3 + border) + 2 * (
                            size - 2 * border) / 6) - tsize
                pygame.draw.rect(screen, white, (startx, starty, tsize * 2, tsize * 2))
                pygame.draw.polygon(screen, black, [[xsize + startx, starty], [tsize * 2 - xsize + startx, starty],
                                                    [centerx, centery - cdist]])
                pygame.draw.polygon(screen, black, [[startx, xsize + starty], [startx, tsize * 2 - xsize + starty],
                                                    [centerx - cdist, centery]])
                pygame.draw.polygon(screen, black, [[xsize + startx, tsize * 2 + starty],
                                                    [tsize * 2 - xsize + startx, tsize * 2 + starty],
                                                    [centerx, centery + cdist]])
                pygame.draw.polygon(screen, black, [[tsize * 2 + startx, xsize + starty],
                                                    [tsize * 2 + startx, tsize * 2 - xsize + starty],
                                                    [centerx + cdist, centery]])
    pygame.display.update()


def checkwin(board):
    cod = [[[0, 0], [1, 0], [2, 0]],
           [[0, 1], [1, 1], [2, 1]],
           [[0, 2], [1, 2], [2, 2]],
           [[0, 1], [0, 2], [0, 0]],
           [[1, 1], [1, 2], [1, 0]],
           [[2, 1], [2, 2], [2, 0]],
           [[0, 0], [1, 1], [2, 2]],
           [[0, 2], [1, 1], [2, 0]]]
    for i in cod:
        streak = True
        for j in i:
            if board[j[0]][j[1]] != 1:
                streak = False
        if streak:
            return 1
        streak = True
        for j in i:
            if board[j[0]][j[1]] != 2:
                streak = False
        if streak:
            return 2
    for i in board:
        for j in i:
            if j == 0:
                return 0
    return 3


def solve(board, next):
    board = ctuple(board)
    winner = checkwin(board)
    if winner == 1:
        dict[(board, next)] = (1, ())
        return (1, ())
    if winner == 2:
        dict[(board, next)] = (-1, ())
        return (-1, ())
    if winner == 3:
        dict[(board, next)] = (0, ())
        return (0, ())
    if next:
        choices = []
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    nboard = clist(board)
                    nboard[i][j] = 1
                    nboard = ctuple(nboard)
                    try:
                        sol = dict[(nboard, False)]
                    except:
                        sol = solve(nboard, False)
                    choices.append([i, j, sol[0]])
        bestmoves = ()
        for i in choices:
            if i[2] == max(choices, key=lambda x: x[2])[2]:
                bestmoves += (i[0], i[1]),
        dict[board, next] = (max(choices, key=lambda x: x[2])[2], bestmoves)
        return (max(choices, key=lambda x: x[2])[2], bestmoves)
    else:
        choices = []
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    nboard = clist(board)
                    nboard[i][j] = 2
                    nboard = ctuple(nboard)
                    try:
                        sol = dict[(nboard, True)]
                    except:
                        sol = solve(nboard, True)
                    choices.append([i, j, sol[0]])
        dict[board, next] = (min(choices, key=lambda x: x[2])[2], ())
        return (min(choices, key=lambda x: x[2])[2], ())


def getclick(size):
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                x = [int((pygame.mouse.get_pos()[0] - sc[0] // 2 + size) // (2 * size / 3)),
                     int((pygame.mouse.get_pos()[1] - sc[1] // 2 + size) // (2 * size / 3))]
                try:
                    if board[x[1]][x[0]] == 0:
                        return x
                except:
                    pass


def end(mode, winner, font):
    if mode == 'p':
        if winner == 1:
            text = 'Player 1 (X) wins!'
        if winner == 2:
            text = 'Player 2 (O) wins!'
        if winner == 3:
            text = 'It\'s a draw!'
    if mode == 'c':
        if winner == 1:
            print(cf)
            text = 'Computer (X) wins!'
        if winner == 2:
            text = 'Player (O) wins!'
        if winner == 3:
            text = 'It\'s a draw!'
    screen.blit(font.render(text, True, (250, 250, 250)), (200, 530))
    pygame.display.update()
    time.sleep(5)


if __name__ == "__main__":

    dict = {}
    solve([[0, 0, 0], [0, 0, 0], [0, 0, 0]], True)
    solve([[0, 0, 0], [0, 0, 0], [0, 0, 0]], False)

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    mode, cf = instructions(font)

    if mode == 'p':
        while True:
            drawboard(board, size, border)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = getclick(size)
            board[pos[1]][pos[0]] = 1
            drawboard(board, size, border)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = getclick(size)
            board[pos[1]][pos[0]] = 2

    if mode == 'c':
        if cf:
            drawboard(board, size, border)
            pos = random.choice(dict[ctuple(board), True][1])
            time.sleep(.5)
            board[pos[0]][pos[1]] = 1
        while True:
            drawboard(board, size, border)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = getclick(size)
            board[pos[1]][pos[0]] = 2
            drawboard(board, size, border)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = random.choice(dict[ctuple(board), True][1])
            time.sleep(.5)
            board[pos[0]][pos[1]] = 1

    end(mode, winner, font)
