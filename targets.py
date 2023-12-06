import random
import math
import pygame


class Targets:
    def __init__(self):
        self.speed = 0.4
        self.cord_x = None
        self.cord_y = None
        self.number_of_targets = 15

        self.targets = []

    def randomize_position(self, number):
        for number in range(number):
            x = random.randint(-400, 1200)
            if x < 0 or x > 800:
                self.cord_x = random.choice([random.randint(-500, -100), random.randint(900, 1300)])
                self.cord_y = random.randint(0, 600)
                size = random.choice([
                    {
                        "size": 15,
                        "life": 10
                    },
                    {
                        "size": 35,
                        "life": 20
                    },
                    {
                        "size": 55,
                        "life": 30
                    }
                ])
                self.targets.append([[self.cord_x, self.cord_y], size])

            elif 0 <= x <= 800:
                self.cord_x = x
                self.cord_y = random.choice([random.randint(-250, -100), random.randint(700, 850)])
                size = random.choice([
                    {
                        "size": 15,
                        "life": 10
                    },
                    {
                        "size": 35,
                        "life": 20
                    },
                    {
                        "size": 55,
                        "life": 30
                    }
                ])
                self.targets.append([[self.cord_x, self.cord_y], size])

        print(self.targets)

    def shooted(self, bullet, rect):
        for target in self.targets:
            if rect == target:
                rect[1]["life"] -= bullet.power
                if rect[1]["life"] <= 0:
                    print(rect)
                    print(self.targets)
                    self.targets.remove(rect)
        # print(rect)
        #
        # rect_xy = [rect.x, rect.y]
        # for target in self.targets:
        #
        #     if target[0] == rect_xy:
        #         print("passou")
        #         target[1]["life"] -= bullet.power
        #         if target[1]["life"] <= 0:
        #             self.targets.remove(rect)

    def create(self, screen, color):
        for target in self.targets:
            pygame.draw.rect(screen, color, (*target[0], target[1]["size"], target[1]["size"]))

    def move_targets_through_center(self, center_x, center_y, target_speed):
        for target in self.targets:
            target_x, target_y = target[0]
            angle = math.atan2(center_y - target_y, center_x - target_x)
            target[0][0] += target_speed * math.cos(angle)
            target[0][1] += target_speed * math.sin(angle)
