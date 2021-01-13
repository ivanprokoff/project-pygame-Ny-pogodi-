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
        self.rect.x = False
        self.rect.y = False
        self.all_positions = {
            0: [(60, 120), (90, 140), (120, 160)],
            1: [(520, 120), (495, 135), (460, 160)],
            2: [(60, 260), (90, 275), (120, 290)],
            3: [(520, 260), (495, 270), (460, 290)]
        }
        self.coords = self.all_positions[random.randint(0, 3)]
        self.index = 0
        self.mask = pygame.mask.from_surface(self.image)

    def choose_position(self):
        self.coords = self.all_positions[random.randint(0, 4)]
        print(self.coords)

    def update(self, screen):
        crd = self.coords[self.index]
        self.rect.x = crd[0]
        self.rect.y = crd[1]

    def update_index(self):
        self.index += 1

    def draw(self, screen):
        if self.rect.x and self.rect.y:
            screen.blit(self.image, (self.rect.x, self.rect.y))
