class Circular :
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"{self.x}, {self.y}")
        
    def Move(self):
        self.x += 1
        self.y += 1


if __name__ == "__main__":
    c = Circular(10, 100, 100)
    
    while True:
        c.draw()
        c.Move()
        