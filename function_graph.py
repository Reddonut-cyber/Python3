import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x

pygame.init()

w = 600
h = 600
N = 300

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

prev_x = None
prev_y = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x in range(-N, N):
        scaled_x = w // 2 + x 
        scaled_y = h // 2 - f(x) 
        if prev_x is not None and prev_y is not None:
            pygame.draw.line(screen, (255, 255, 255), (prev_x , prev_y), (scaled_x, scaled_y))
            
        prev_x, prev_y = scaled_x, scaled_y
        #screen.set_at((p_x), (255, 255, 255))
        # pygame.draw.line(screen, (0, 255, 0), (10, 10), (300, 300))

    pygame.display.flip()

pygame.quit()