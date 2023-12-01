import time
import pygame
import sys
import math
from bullet import Bullet
from square import Square
from targets import Targets

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player = Square(WIDTH, HEIGHT)
bullet = Bullet()
targets = Targets()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clique no Quadrado")
clock = pygame.time.Clock()


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


while True:
    pressing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bullet.shoot(player.x, player.y, player.size, player.angle)
            if event.key == pygame.K_x:
                targets.randomize_position(10)

    targets.move_targets_to_center(WIDTH // 2, HEIGHT // 2, targets.speed)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.rotation("right")
    if keys[pygame.K_LEFT]:
        player.rotation("left")

    for projectile in bullet.list[:]:
        projectile[0] += bullet.speed * math.cos(math.radians(projectile[2]))
        projectile[1] += bullet.speed * math.sin(math.radians(projectile[2]))

        bullet_rect = pygame.Rect(projectile[0], projectile[1], bullet.size, bullet.size)

        for target in targets.targets[:]:
            target_rect = pygame.Rect(*target[0], target[1], target[1])
            if check_collision(bullet_rect, target_rect):
                # Se houver colisão, remove o projétil e o alvo
                bullet.list.remove(projectile)
                targets.targets.remove(target)
                break

    screen.fill(BLACK)

    for projectile in bullet.list[:]:
        pygame.draw.rect(screen, WHITE, (projectile[0], projectile[1], bullet.size, bullet.size))

    for target in targets.targets[:]:
        targets.create(screen, WHITE)

    player.draw_rotated_square(screen, WHITE, player.x, player.y, player.angle)

    pygame.display.flip()

    clock.tick(FPS)
