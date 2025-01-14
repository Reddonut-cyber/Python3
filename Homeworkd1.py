import pygame
import random

class Circular:
    def __init__(self, radius, x, y, vx, vy, color):
        self.radius = radius
        self.color = color  
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, window_width, window_height):
        self.x += self.vx
        self.y += self.vy

        # Check for collisions with window edges
        if self.x + self.radius >= window_width or self.x - self.radius <= 0:
            self.vx = -self.vx
        if self.y + self.radius >= window_height or self.y - self.radius <= 0:
            self.vy = -self.vy

if __name__ == "__main__":
    pygame.init()

    # Window settings
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Multiple Circles Game")

    # Colors
    background_color = (0, 0, 0)  # Black

    # Initialize multiple circles
    circles = []
    for _ in range(10):  # Create circles
        radius = random.randint(10, 30)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(radius, window_width - radius)
        y = random.randint(radius, window_height - radius)
        vx = random.randint(-5, 8)
        vy = random.randint(-5, 8)
        circles.append(Circular(radius, x, y, vx, vy, color))

    # Clock for controlling frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move and draw all circles
        screen.fill(background_color)
        for circle in circles:
            circle.move(window_width, window_height)
            circle.draw(screen)

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()
