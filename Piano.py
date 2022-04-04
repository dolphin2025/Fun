import pygame
pygame.init()

import winsound


# --------------------------------------

print('C major octaves from A-K and 1-8. Black keys below.')

s = [round(261.63), round(277.18), round(293.66), round(311.13), round(329.63), round(349.23),  # C to F
     round(369.99), round(392.00), round(415.30), round(440.00), round(466.16), round(493.88),  # F sharp to B
     round(523.25), round(554.37), round(587.33), round(622.25), round(659.25), round(698.46),  # C to F
     round(739.99), round(783.99), round(830.61), round(880.00), round(932.33), round(987.77),  # F sharp to B
     round(1046.50), round(1108.73), round(1174.66), round(1244.51), round(1318.51)]  # C to E

screen_coord = (800, 600)
screen = pygame.display.set_mode(screen_coord)

while True:
    time = 200
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        winsound.Beep(s[0], time)  # C
    if keys[pygame.K_z]:
        winsound.Beep(s[1], time)
    if keys[pygame.K_s]:
        winsound.Beep(s[2], time)
    if keys[pygame.K_x]:
        winsound.Beep(s[3], time)
    if keys[pygame.K_d]:
        winsound.Beep(s[4], time)
    if keys[pygame.K_f]:
        winsound.Beep(s[5], time)
    if keys[pygame.K_v]:
        winsound.Beep(s[6], time)
    if keys[pygame.K_g]:
        winsound.Beep(s[7], time)
    if keys[pygame.K_b]:
        winsound.Beep(s[8], time)
    if keys[pygame.K_h]:
        winsound.Beep(s[9], time)
    if keys[pygame.K_n]:
        winsound.Beep(s[10], time)
    if keys[pygame.K_j]:
        winsound.Beep(s[11], time)
    if keys[pygame.K_k]:
        winsound.Beep(s[12], time)  # C

    if keys[pygame.K_1]:
        winsound.Beep(s[12], time)  # C
    if keys[pygame.K_q]:
        winsound.Beep(s[13], time)
    if keys[pygame.K_2]:
        winsound.Beep(s[14], time)
    if keys[pygame.K_w]:
        winsound.Beep(s[15], time)
    if keys[pygame.K_3]:
        winsound.Beep(s[16], time)
    if keys[pygame.K_4]:
        winsound.Beep(s[17], time)
    if keys[pygame.K_r]:
        winsound.Beep(s[18], time)
    if keys[pygame.K_5]:
        winsound.Beep(s[19], time)
    if keys[pygame.K_t]:
        winsound.Beep(s[20], time)
    if keys[pygame.K_6]:
        winsound.Beep(s[21], time)
    if keys[pygame.K_y]:
        winsound.Beep(s[22], time)
    if keys[pygame.K_7]:
        winsound.Beep(s[23], time)
    if keys[pygame.K_8]:
        winsound.Beep(s[24], time)  # C
    if keys[pygame.K_i]:
        winsound.Beep(s[25], time)
    if keys[pygame.K_9]:
        winsound.Beep(s[26], time)
    if keys[pygame.K_o]:
        winsound.Beep(s[27], time)
    if keys[pygame.K_0]:
        winsound.Beep(s[28], time)  # E
