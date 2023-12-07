import pygame


class Bullet:
    def __init__(self):
        self.size = 3
        self.speed = 5
        self.power = 10
        self.list = []
        self.last_shot_time = 0
        self.attack_speed = 700

    def shoot(self, x, y, size, angle):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.attack_speed:
            self.last_shot_time = current_time
            bullet_x = x + size // 2 - self.size // 2
            bullet_y = y + size // 2 - self.size // 2
            self.list.append([bullet_x, bullet_y, angle])
        else:
            return None

    def collided(self, rect):
        for bullet in self.list:
            if bullet == rect:
                self.list.remove(bullet)
