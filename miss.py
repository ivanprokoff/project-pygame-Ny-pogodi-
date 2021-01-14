import pygame
from loading import load_image


class Miss(pygame.sprite.Sprite):
    # Изображение при промахе (цыпленок)
    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('miss_pict.jpg', color_key=-1), (97, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 20

    def update(self):
        # Смена координат изображения при промахе
        self.rect.x += 70
