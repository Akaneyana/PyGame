import pygame
import sys
import time
import random

#start using pygame
pygame.init()

# how big the screen is
res = (720, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Reaction Time Test")

# what font i am using
font = pygame.font.SysFont('Rubik-Regular.ttf', 90)

title = font.render("Reaction Time")


# runs pygame into a game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()