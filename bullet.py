class Bullet:
    def __init__(self):
        self.size = 3
        self.speed = 5
        self.list = []

    def shoot(self, x, y, size, angle):
        bullet_x = x + size // 2 - self.size // 2
        bullet_y = y + size // 2 - self.size // 2
        self.list.append([bullet_x, bullet_y, angle])
