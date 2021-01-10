import pygame
from loading import load_image
import random


class Egg(pygame.sprite.Sprite):
    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = load_image("newEgg.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.all_positions = {
            'left_up': [(60, 120), (90, 140), (120, 160)],
            'right_up': [(520, 120), (495, 135), (460, 160)],
            'left_down': [(60, 260), (90, 275), (120, 290)],
            'right_down': [(520, 260), (495, 270), (460, 290)]
        }
        self.position_list = ['left_up', 'right_up', 'left_down', 'right_down']
        self.coords = ''
        self.index = 0

    def choose_position(self):
        self.coords = self.all_positions[random.choice(self.position_list)]

    def update(self, screen):
        crd = self.coords[self.index]
        self.rect.x = crd[0]
        self.rect.y = crd[1]

    def update_index(self):
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, (100, 100))
