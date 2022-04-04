import pygame
import sys
import time
import math

sc = (800, 600)
screen = pygame.display.set_mode(sc)
sqsize = 60  # 60
border = 5  # 5
xpos = 185  # 185
ypos = 200  # 200
lw = 10  # 10
dlw = int(lw * math.sqrt(2) / 4)
pygame.init()
font = pygame.font.SysFont("comicsansms", 20)

black = (20, 20, 20)
white = (250, 250, 250)
red = (240, 40, 40)
yellow = (238, 230, 0)
blue = (30, 144, 255)


def instructions(font):
    print()
    print('NOTE:')
    print('If you see a pygame message but no window, you may have to find the window on your computer.')
    dist = 25
    ins = ['Welcome to Pahan\'s Python Connect4 (7x6) Game! ',
           'Currently, only 2-player is available',
           'To place your piece, click on the column you would like to place your piece in.',
           'The player who gets 4 in a row (vertical, horizontal, diagonal) first wins.',
           'Remember that there gravity exists!',
           'Press p to play!']

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
        ins = ['1=you first, 2=me first',
               'Press the corresponding key from above.']
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


def drawboard(board, border, sqsize, xpos, ypos):
    pygame.draw.rect(screen, black, (0, 0, sc[0], sc[1]))
    pygame.draw.rect(screen, white, (xpos - border, ypos - border, 7 * sqsize + 2 * border, 6 * sqsize + 2 * border))
    for i in range(0, 7):
        for j in range(0, 6):
            color = [black, red, yellow][board[j][i]]
            pygame.draw.circle(screen, color, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5))),
                               sqsize // 2 - border)
    pygame.display.update()


def checkwin(board):
    for i in range(0, 7):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i] == board[j][i] and board[j + 2][i] == board[j + 1][i] and \
                    board[j + 3][i] == board[j + 2][i]:
                return board[j][i]
    for i in range(0, 4):
        for j in range(0, 6):
            if board[j][i] != 0 and board[j][i + 1] == board[j][i] and board[j][i + 2] == board[j][i + 1] and board[j][
                i + 3] == board[j][i + 2]:
                return board[j][i]
    for i in range(0, 4):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i + 1] == board[j][i] and board[j + 2][i + 2] == board[j + 1][
                i + 1] and board[j + 3][i + 3] == board[j + 2][i + 2]:
                return board[j][i]
    for i in range(3, 7):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i - 1] == board[j][i] and board[j + 2][i - 2] == board[j + 1][
                i - 1] and board[j + 3][i - 3] == board[j + 2][i - 2]:
                return board[j][i]
    for i in board:
        for j in i:
            if j == 0:
                return 0
    return 3


def compmove(board, cf, next, depth):
    if depth == 0:
        hcomp, hhum = 0, 0
        for i in range(0, 7):
            for j in range(0, 3):
                r = [board[j][i], board[j + 1][i], board[j + 2][i], board[j + 3][i]]
                if r.count(0) == 1:
                    if r.count(1) == 3:
                        hcomp += 1
                    elif r.count(2) == 3:
                        hhum += 1
        for i in range(0, 4):
            for j in range(0, 6):
                r = [board[j][i], board[j][i + 1], board[j][i + 2], board[j][i + 3]]
                if r.count(0) == 1:
                    if r.count(1) == 3:
                        hcomp += 1
                    elif r.count(2) == 3:
                        hhum += 1
        for i in range(0, 4):
            for j in range(0, 3):
                r = [board[j][i], board[j + 1][i + 1], board[j + 2][i + 2], board[j + 3][i + 3]]
                if r.count(0) == 1:
                    if r.count(1) == 3:
                        hcomp += 1
                    elif r.count(2) == 3:
                        hhum += 1
        for i in range(3, 7):
            for j in range(0, 3):
                r = [board[j][i], board[j + 1][i - 1], board[j + 2][i - 2], board[j + 3][i - 3]]
                if r.count(0) == 1:
                    if r.count(1) == 3:
                        hcomp += 1
                    elif r.count(2) == 3:
                        hhum += 1
        return [(hcomp - hhum) / 100]

    if next:
        scores = []
        for move in range(0, 7):
            if board[5][move] == 0:
                nboard = board[:]
                for i in range(5, -1, -1):
                    if board[i][move] == 0:
                        nboard[i][move] = 1
                        pos = i
                        break
                winner = checkwin(nboard)
                if winner != 0:
                    if winner == 1:
                        return [1, move, pos]
                    if winner == 2:
                        scores.append([-1, move, pos])
                        continue
                    if winner == 0:
                        scores.append([0, move, pos])
                        continue
                scores.append([compmove(nboard, cf, not (next), depth - 1)[0], move, pos])

        print(board, cf, next, depth)
        return max(scores, key=lambda x: x[0])

    scores = []
    for move in range(0, 7):
        if board[5][move] == 0:
            nboard = board[:]
            for i in range(5, -1, -1):
                if board[i][move] == 0:
                    nboard[i][move] = 2
                    pos = i
                    break
            winner = checkwin(nboard)
            if winner != 0:
                if winner == 1:
                    scores.append([1, move, pos])
                    continue
                if winner == 2:
                    return [-1, move, pos]
                if winner == 0:
                    scores.append([0, move, pos])
                    continue
            scores.append(compmove(nboard, cf, not (next), depth - 1))
    return min(scores, key=lambda x: x[0])


def humanmove(board, xpos):
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x = max((pygame.mouse.get_pos()[0] - xpos) // sqsize, 0)
                try:
                    for i in range(5, -1, -1):
                        if board[i][x] == 0:
                            return x, i
                except:
                    pass


def end(mode, winner, font):
    for i in range(0, 7):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i] == board[j][i] and board[j + 2][i] == board[j + 1][i] and \
                    board[j + 3][i] == board[j + 2][i]:
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5))),
                                   lw // 2)
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + 3.5))),
                                   lw // 2)
                pygame.draw.rect(screen, blue, (
                xpos + int(sqsize * (i + .5)) - lw // 2, ypos + int(sqsize * (j + .5)), lw, 3 * sqsize))
    for i in range(0, 4):
        for j in range(0, 6):
            if board[j][i] != 0 and board[j][i + 1] == board[j][i] and board[j][i + 2] == board[j][i + 1] and board[j][
                i + 3] == board[j][i + 2]:
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5))),
                                   lw // 2)
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + 3.5)), ypos + int(sqsize * (j + .5))),
                                   lw // 2)
                pygame.draw.rect(screen, blue, (
                xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5)) - lw // 2, 3 * sqsize, lw))
    for i in range(0, 4):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i + 1] == board[j][i] and board[j + 2][i + 2] == board[j + 1][
                i + 1] and board[j + 3][i + 3] == board[j + 2][i + 2]:
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5))),
                                   lw // 2)
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + 3.5)), ypos + int(sqsize * (j + 3.5))),
                                   lw // 2)
                pygame.draw.polygon(screen, blue, (
                (xpos + int(sqsize * (i + .5)) + dlw + 3 * sqsize, ypos + int(sqsize * (j + .5)) - dlw + 3 * sqsize),
                (xpos + int(sqsize * (i + .5)) - dlw + 3 * sqsize, ypos + int(sqsize * (j + .5)) + dlw + 3 * sqsize),
                (xpos + int(sqsize * (i + .5)) - dlw, ypos + int(sqsize * (j + .5)) + dlw),
                (xpos + int(sqsize * (i + .5)) + dlw, ypos + int(sqsize * (j + .5)) - dlw)))
    for i in range(3, 7):
        for j in range(0, 3):
            if board[j][i] != 0 and board[j + 1][i - 1] == board[j][i] and board[j + 2][i - 2] == board[j + 1][
                i - 1] and board[j + 3][i - 3] == board[j + 2][i - 2]:
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i + .5)), ypos + int(sqsize * (j + .5))),
                                   lw // 2)
                pygame.draw.circle(screen, blue, (xpos + int(sqsize * (i - 2.5)), ypos + int(sqsize * (j + 3.5))),
                                   lw // 2)
                pygame.draw.polygon(screen, blue, (
                (xpos + int(sqsize * (i + .5)) - dlw - 3 * sqsize, ypos + int(sqsize * (j + .5)) - dlw + 3 * sqsize),
                (xpos + int(sqsize * (i + .5)) + dlw - 3 * sqsize, ypos + int(sqsize * (j + .5)) + dlw + 3 * sqsize),
                (xpos + int(sqsize * (i + .5)) + dlw, ypos + int(sqsize * (j + .5)) + dlw),
                (xpos + int(sqsize * (i + .5)) - dlw, ypos + int(sqsize * (j + .5)) - dlw)))
    if mode == 'p':
        if winner == 1:
            text = 'Player 1 (Red) wins!.'
        if winner == 2:
            text = 'Player 2 (Yellow) wins!.'
        if winner == 3:
            text = 'It\'s a draw!.'
    if mode == 'c':
        if winner == 1:
            text = 'Computer (Yellow) wins!.'
        if winner == 2:
            text = 'Player (Red) wins!.'
        if winner == 3:
            text = 'It\'s a draw!.'
    screen.blit(font.render(text, True, (250, 250, 250)), (150, 90))
    pygame.display.update()
    time.sleep(5)


if __name__ == "__main__":

    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

    mode, cf = instructions(font)

    if mode == 'p':
        while True:
            drawboard(board, border, sqsize, xpos, ypos)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = humanmove(board, xpos)
            board[pos[1]][pos[0]] = 1
            drawboard(board, border, sqsize, xpos, ypos)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = humanmove(board, xpos)
            board[pos[1]][pos[0]] = 2
    else:
        if cf:
            drawboard(board, border, sqsize, xpos, ypos)
            cmove = compmove(board[:], cf, True, 4)
            board[cmove[2]][cmove[1]] = 1
        while True:
            drawboard(board, border, sqsize, xpos, ypos)
            winner = checkwin(board)
            if winner != 0:
                break
            pos = humanmove(board, xpos)
            board[pos[1]][pos[0]] = 1
            drawboard(board, border, sqsize, xpos, ypos)
            cmove = compmove(board[:], cf, True, 4)
            board[cmove[2]][cmove[1]] = 1

    end(mode, winner, font)
