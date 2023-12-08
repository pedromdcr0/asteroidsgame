import json
import random
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class PowerUps:
    def __init__(self):
        self.options = []
        self.selected_option = 1
        self.text = None
        self.font = pygame.font.Font("font.ttf", 30)
        self.font_size = 25
        self.color = RED
        self.option_texts = [self.font.render(option, True, self.color) for option in self.options]
        self.menu = False

    def choose(self, screen, width, height):
        self.menu = True

        options = []
        with open("powerups.json", "r") as powerups_file:
            powerups_data = json.load(powerups_file)
            for powerup in powerups_data:
                options.append(powerup)
        print(random.sample(options, 3))
        player_options = random.sample(options, 3)
        player_options_names = []
        self.options = player_options_names

        for index, text in enumerate(player_options):
            print(index)
            if index + 1 == self.selected_option:
                self.color = WHITE
                self.font_size = 35
                player_options_names.append(text["name"])
                # text2 = self.font.render(self.text, True, self.color)
        for i, text in enumerate(self.option_texts):
            screen.blit(text, (width // 2, height // 2))

            # screen.blit(text2, (width // 2, height // 4))

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
                print(f"Opção selecionada: {self.options[self.selected_option]}")
                self.menu = False  # Saia do menu depois de escolher
