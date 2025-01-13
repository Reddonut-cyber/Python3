class Circular :
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y 
        
    def draw(self):
        print(f"{self.x}, {self.y}")
        
    def Move(self, radius, x, y):
        self.radius = radius
        self.x = x + 1
        self.y = y + 1

if __name__ == "__main__":
    c = Circular(10, 100, 100)
    c.draw()