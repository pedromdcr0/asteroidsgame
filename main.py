import pygame
import sys

import math
from square import Square

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

player = Square(WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clique no Quadrado")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.projectiles.append((player.x, player.y, player.angle))

    keys = pygame.key.get_pressed()

    player.angle += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player.speed

    for projectile in player.projectiles:
        projectile_x, projectile_y, projectile_angle = projectile
        projectile_x += player.projectile_speed * math.cos(math.radians(projectile_angle))
        projectile_y -= player.projectile_speed * math.sin(math.radians(projectile_angle))
        pygame.draw.rect(screen, RED, (projectile_x, projectile_y, player.projectile_size, player.projectile_size))

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player.x, player.y, player.size, player.size))

    pygame.display.flip()

    clock.tick(FPS)
