import pygame
import sys
import math
from bullet import Bullet
from square import Square
from targets import Targets
from power_ups import PowerUps

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player = Square(WIDTH, HEIGHT)
power_ups = PowerUps()
bullet = Bullet()
targets = Targets()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rogueroids")
clock = pygame.time.Clock()

score = 0
game_active = False
game_is_on = True
level_completed = 0
level = 0
menu = False
current_time = pygame.time.get_ticks()


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


def increase_level(level_number):
    global level
    level += 1
    targets.shooted_targets.clear()
    level_multiply = level_number / 1.3
    life_multiply = level_number % 10
    if level_number < 10:
        target_multiply = 1.5
    else:
        target_multiply = 1.125

    if level > 1:
        targets.speed *= (1.2 * level_multiply)
    elif level >= 0:
        targets.speed = targets.speed
    for target_type in targets.sizelife:
        target_type["life"] *= float(f"1.0{life_multiply}")

    targets.number_of_targets *= target_multiply


while game_is_on:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                if level == 0:
                    increase_level(level)
                    game_active = True

    if game_active:
        print("game is active, showing player and targets moving to center")
        print(targets.created_targets, level_completed)
        player.draw_rotated_square(screen, WHITE, player.x, player.y, player.angle)
        targets.move_targets_through_center(WIDTH // 2, HEIGHT // 2, targets.speed)

        if level_completed == 1:
            print("level was completed, turning game active to false")
            game_active = False

        if not targets.created_targets and level_completed == 0:
            print("creating targets")
            targets.randomize_position(targets.number_of_targets_final, level_completed)

        if len(targets.shooted_targets) == targets.number_of_targets_final:
            print(len(targets.shooted_targets), targets.number_of_targets_final)
            game_active = False
            level_completed = 1
            menu = True
            # print(str(game_active) + "is gameactive?")
            # print(str(level_completed) + "level completed?")
            print("game active turned false, level completed turned 1, menu turned true")

        # if targets.created_targets:
        #     pass

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player.rotation("right")
        if keys[pygame.K_LEFT]:
            player.rotation("left")
        if keys[pygame.K_UP]:
            player.rotation("up")
        if keys[pygame.K_DOWN]:
            player.rotation("down")
        if keys[pygame.K_SPACE]:
            bullet.shoot(player.x, player.y, player.size, player.angle)

        for projectile in bullet.list:
            projectile[0] += bullet.speed * math.cos(math.radians(projectile[2]))
            projectile[1] += bullet.speed * math.sin(math.radians(projectile[2]))

            bullet_rect = pygame.Rect(projectile[0], projectile[1], bullet.size, bullet.size)

            for target in targets.targets:
                target_rect = pygame.Rect(*target[0], target[1]["size"], target[1]["size"])
                if check_collision(bullet_rect, target_rect):
                    bullet.collided(projectile)
                    targets.shooted(bullet, target)

        for projectile in bullet.list:
            pygame.draw.rect(screen, WHITE, (projectile[0], projectile[1], bullet.size, bullet.size))

        for target in targets.targets:
            targets.create(screen, WHITE)

    if not game_active:
        if level == 0:
            print("level == 0")
            font = pygame.font.Font("font.ttf", 20)
            text = font.render("Rogueroids", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

            score_text = font.render(f"High Score: {score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

            restart_text = font.render("Pressione SPACE para jogar", True, WHITE)
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 3 * HEIGHT // 4))

        if level_completed == 1 and menu:
            print("if level_completed == 1 and menu:")
            while menu:

                increase_level(level)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            power_ups.choose(screen, WIDTH, HEIGHT, menu, "up")
                        elif event.key == pygame.K_DOWN:
                            power_ups.choose(screen, WIDTH, HEIGHT, menu, "down")
                        elif event.key == pygame.K_x:
                            power_ups.choose(screen, WIDTH, HEIGHT, menu, "x")
                            level_completed = 0
                            game_active = True
                            menu = False

    pygame.display.flip()
    clock.tick(FPS)
