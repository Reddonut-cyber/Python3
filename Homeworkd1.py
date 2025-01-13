import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circle")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


x, y = WIDTH // 2, HEIGHT // 2  
radius = 30                     
velocity_x, velocity_y = 5, 3   

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += velocity_x
    y += velocity_y

    if x - radius <= 0 or x + radius >= WIDTH: 
        velocity_x = -velocity_x
    if y - radius <= 0 or y + radius >= HEIGHT: 
        velocity_y = -velocity_y

    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (x, y), radius) 
    pygame.display.flip()  

    clock.tick(60)
