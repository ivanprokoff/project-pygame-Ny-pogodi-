import random
import pygame
from loading import load_image


class Wolf(pygame.sprite.Sprite):
    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = load_image("wolf_main_left.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100

    def update(self, key):
        if key == 'right':
            self.image = load_image("wolf_main_right.png")
        elif key == 'left':
            self.image = load_image("wolf_main_left.png")
