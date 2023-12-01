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
    pressing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.projectiles.append((player.x, player.y, player.angle))
    if keys[pygame.K_RIGHT]:
        player.rotation("right")
    if keys[pygame.K_LEFT]:
        player.rotation("left")

    for projectile in player.projectiles:
        projectile_x, projectile_y, projectile_angle = projectile
        projectile_x += player.projectile_speed * math.cos(math.radians(projectile_angle))
        projectile_y -= player.projectile_speed * math.sin(math.radians(projectile_angle))
        pygame.draw.rect(screen, RED, (projectile_x, projectile_y, player.projectile_size, player.projectile_size))

    screen.fill(WHITE)

    player.draw_rotated_square(screen, RED, player.x, player.y, player.angle)

    pygame.display.flip()

    clock.tick(FPS)
