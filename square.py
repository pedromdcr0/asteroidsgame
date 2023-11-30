import pygame


class Square:
    def __init__(self, width, height):
        self.size = 10
        self.angle = 0
        self.speed = 5
        self.x = (width // 2) - self.size
        self.y = (height // 2) - self.size
        self.projectile_size = 3
        self.projectile_speed = 10
        self.projectiles = []

    def shoot(self):
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE:
                pass


