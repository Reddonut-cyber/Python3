class Circular :
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"{self.x}, {self.y}")
        
    def Move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y
            

if __name__ == "__main__":
    c = Circular(10, 50, 20)
    vx = 1
    vy = 1
    window_width = 100
    window_height = 100
    
    for i in range(100):
        if c.x >= window_width or c.x <= 0:
            vx =-vx
        if c.y >= window_height or c.y <= 0:
            vy = -vy
        c.draw()
        c.Move(vx,vy)