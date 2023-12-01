import pygame
import math

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

    def rotation(self, rl):
        if rl == "right":
            if self.angle == 355:
                self.angle = 0
            else:
                self.angle += 5
        elif rl == "left":
            if self.angle == 0:
                self.angle = 355
            else:
                self.angle -= 5

    def draw_rotated_square(self, surface, color, x, y, angle):
        half_size = self.size // 2
        vertices = [
            (x - half_size, y - half_size),
            (x + half_size, y - half_size),
            (x + half_size, y + half_size),
            (x - half_size, y + half_size)
        ]
        rotated_vertices = []
        for vertex in vertices:
            rotated_x = x + math.cos(math.radians(angle)) * (vertex[0] - x) - math.sin(math.radians(angle)) * (
                        vertex[1] - y)
            rotated_y = y + math.sin(math.radians(angle)) * (vertex[0] - x) + math.cos(math.radians(angle)) * (
                        vertex[1] - y)
            rotated_vertices.append((rotated_x, rotated_y))

        pygame.draw.polygon(surface, color, rotated_vertices, 0)


