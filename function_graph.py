import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x ** 2

pygame.init()

w = 800
h = 800
x_max = 2
x_min = -2
scale = 30
step = 0.01

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))
    
    prev_x = None
    prev_y = None
    x = x_min
    while x <= x_max:
        scaled_x = int(w / 2) + int(x * scale) 
        scaled_y = int(h / 2) - int(f(x) * scale)
        if prev_x is not None and prev_y is not None:
            pygame.draw.line(screen, (255, 255, 255), (prev_x , prev_y), (scaled_x, scaled_y))
            
            
        prev_x, prev_y = scaled_x, scaled_y
        x += step
        #screen.set_at((p_x), (255, 255, 255))
        # pygame.draw.line(screen, (0, 255, 0), (10, 10), (300, 300))

    pygame.display.flip()

pygame.quit()
logger.info("Program terminated")