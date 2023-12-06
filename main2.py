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
pygame.display.set_caption("Rogueroids")
clock = pygame.time.Clock()

score = 0
game_active = True
game_is_on = True
level_completed = 0
level = 1


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


def increase_level(level_number):
    level_multiply = level_number / 1.3
    life_multiply = level_number % 10
    if level_number < 10:
        target_multiply = 1.5
    else:
        target_multiply = 1.125

    targets.speed *= (1.2 * level_multiply)
    for target_type in targets.sizelife:
        target_type["life"] *= int(f"1.0{life_multiply}")

    targets.number_of_targets *= target_multiply


while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if level_completed == 1:
        level += 1
        increase_level(level)
        level_completed = 0

    if game_active and level_completed == 0 and len(targets.targets) == 0:
        level_completed = 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.rotation("right")
    if keys[pygame.K_LEFT]:
        player.rotation("left")
    if keys[pygame.K_UP]:
        player.rotation("up")
    if keys[pygame.K_DOWN]:
        player.rotation("down")

    for projectile in bullet.list[:]:
        projectile[0] += bullet.speed * math.cos(math.radians(projectile[2]))
        projectile[1] += bullet.speed * math.sin(math.radians(projectile[2]))

        bullet_rect = pygame.Rect(projectile[0], projectile[1], bullet.size, bullet.size)

        for target in targets.targets:
            target_rect = pygame.Rect(*target[0], target[1]["size"], target[1]["size"])
            if check_collision(bullet_rect, target_rect):
                bullet.collided(projectile)
                targets.shooted(bullet, target)
