import json
import random
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class PowerUps:
    def __init__(self):
        self.selected_option = 1
        self.font_size = 20
        self.font = pygame.font.Font("font.ttf", self.font_size)
        self.color = RED
        self.option_texts = self.font.render("text", True, self.color)
        self.menu = False
        self.powerup_chosed = False

    def choose(self, screen, width, height, menu):
        self.menu = True
        if menu and self.menu:
            options = []
            player_options = []

            if not self.powerup_chosed:

                with open("powerups.json", "r") as powerups_file:
                    powerups_data = json.load(powerups_file)
                    for powerup in powerups_data:
                        options.append(powerup)
                player_options = random.sample(options, 3)
                self.powerup_chosed = True

            for index, text in enumerate(player_options):
                print(index)
                if index + 1 == self.selected_option:
                    self.font_size = 50
                    texto = self.font.render(text["name"], True, WHITE)
                    screen.blit(texto, (width // 2 - texto.get_width() // 2, height // 2 + index * 50))
                elif index + 1 != self.selected_option:
                    self.color = RED
                    self.font_size = 20
                    texto = self.font.render(text["name"], True, self.color)
                    screen.blit(texto, (width // 2 - texto.get_width() // 2, height // 2 + index * 50))

    def handle_input(self, key_event):
        if key_event == "up":
            if self.selected_option == 1:
                self.selected_option = 3
                print(self.selected_option)
            else:
                self.selected_option -= 1
                print(self.selected_option)
        elif key_event == "down":
            if self.selected_option == 3:
                self.selected_option = 1
                print(self.selected_option)
            else:
                self.selected_option += 1
                print(self.selected_option)
        elif key_event == "x":
            # print(f"Opção selecionada: {self.options[self.selected_option]}")
            self.menu = False  # Saia do menu depois de escolher
            return False
