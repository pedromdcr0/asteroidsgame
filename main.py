import pygame
import sys
import random
import math
from square import Square

# Inicialização do Pygame
pygame.init()


# Configurações do jogo
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

player = Square(WIDTH, HEIGHT)

# Configuração da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clique no Quadrado")
clock = pygame.time.Clock()

# Variáveis do jogo


# Loop principal do jogo
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

    # Atualizar a tela
    pygame.display.flip()

    # Definir a taxa de quadros por segundo
    clock.tick(FPS)
