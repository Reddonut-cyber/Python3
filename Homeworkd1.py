import pygame
import random

class Circular:
    def __init__(self, radius, x, y, vx, vy):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

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
    window_width = 400
    window_height = 400
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Multiple Circles Game")

    # Colors
    background_color = (0, 0, 0)  # Black
    circle_color = (255, 255, 255)  # White

    # Initialize multiple circles
    circles = []
    for _ in range(5):  # Create 5 circles
        radius = random.randint(10, 20)
        x = random.randint(radius, window_width - radius)
        y = random.randint(radius, window_height - radius)
        vx = random.choice([-1, 1]) * random.randint(1, 3)
        vy = random.choice([-1, 1]) * random.randint(1, 3)
        circles.append(Circular(radius, x, y, vx, vy))

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
            circle.draw(screen, circle_color)

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()
