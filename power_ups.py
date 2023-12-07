import pygame
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class PowerUps:
    def __init__(self):
        self.options = ["Power Up 1", "Power Up 2", "Power Up 3"]
        self.selected_option = 1
        self.font = pygame.font.Font("font.ttf", 30)
        self.font_size = 25
        self.color = RED
        self.option_texts = [self.font.render(option, True, self.color) for option in self.options]
        self.menu = False

    def choose(self, screen, width, height):
        self.menu = True

        for i, text in enumerate(self.option_texts):
            if i == self.selected_option:
                self.color = WHITE
                self.font_size = 35
            else:
                pass
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 4 + i * 50))

    def handle_input(self, key_event):
        if key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_UP:
                if self.selected_option == 1:
                    self.selected_option = 3
                else:
                    self.selected_option -= 1
            elif key_event.key == pygame.K_DOWN:
                if self.selected_option == 3:
                    self.selected_option = 1
                else:
                    self.selected_option += 1
            elif key_event.key == pygame.K_SPACE:
                # Implemente a lógica para a opção selecionada
                print(f"Opção selecionada: {self.options[self.selected_option]}")
                self.menu = False  # Saia do menu depois de escolher
