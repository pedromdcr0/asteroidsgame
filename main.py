import time
import pygame
import sys
import math
from bullet import Bullet
from square import Square

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player = Square(WIDTH, HEIGHT)
bullet = Bullet()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clique no Quadrado")
clock = pygame.time.Clock()

while True:
    pressing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bullet.shoot(player.x, player.y, player.size, player.angle)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.rotation("right")
    if keys[pygame.K_LEFT]:
        player.rotation("left")

    for projectile in bullet.list:
        projectile[0] += bullet.speed * math.cos(math.radians(projectile[2]))
        projectile[1] += bullet.speed * math.sin(math.radians(projectile[2]))

    screen.fill(WHITE)

    for projectile in bullet.list:
        pygame.draw.rect(screen, BLUE, (projectile[0], projectile[1], bullet.size, bullet.size))

    player.draw_rotated_square(screen, RED, player.x, player.y, player.angle)

    pygame.display.flip()

    clock.tick(FPS)
