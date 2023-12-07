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
number_of_targets = 3
game_active = False


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and game_active:
                bullet.shoot(player.x, player.y, player.size, player.angle)
            elif event.key == pygame.K_x:
                if game_active:
                    targets.randomize_position(round(number_of_targets), 0)
                else:
                    # Se o jogo estiver inativo (Game Over), reinicie o jogo
                    game_active = True
                    score = 0

    targets.move_targets_through_center(WIDTH // 2, HEIGHT // 2, targets.speed)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.rotation("right")
    if keys[pygame.K_LEFT]:
        player.rotation("left")
    if keys[pygame.K_UP]:
        player.rotation("up")
    if keys[pygame.K_DOWN]:
        player.rotation("down")

    for projectile in bullet.list:
        projectile[0] += bullet.speed * math.cos(math.radians(projectile[2]))
        projectile[1] += bullet.speed * math.sin(math.radians(projectile[2]))

        bullet_rect = pygame.Rect(projectile[0], projectile[1], bullet.size, bullet.size)

        #targets_to_remove = []  # Lista temporária para armazenar os projéteis a serem removidos

        for target in targets.targets:
            target_rect = pygame.Rect(*target[0], target[1]["size"], target[1]["size"])
            if check_collision(bullet_rect, target_rect):
                bullet.collided(projectile)
                targets.shooted(bullet, target)
                #targets_to_remove.append(target)

        # Remover os projéteis após o loop interno
        # for projectile2 in targets_to_remove:
        #     #print(projectile2)
        #     if projectile2[1]["life"] <= 0:
        #         #print(projectile2)
        #         #print(targets_to_remove)
        #         targets.targets.remove(projectile2)

    screen.fill(BLACK)

    for projectile in bullet.list[:]:
        pygame.draw.rect(screen, WHITE, (projectile[0], projectile[1], bullet.size, bullet.size))

    for target in targets.targets[:]:
        targets.create(screen, WHITE)

    player.draw_rotated_square(screen, WHITE, player.x, player.y, player.angle)

    if not game_active:
        # Se for Game Over, exiba a tela de Game Over
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

        restart_text = font.render("Pressione X para jogar novamente", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 3 * HEIGHT // 4))

    pygame.display.flip()

    clock.tick(FPS)
