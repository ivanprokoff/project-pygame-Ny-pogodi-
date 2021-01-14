import pygame
import random
from PIL import Image
import os


class Egg(pygame.sprite.Sprite):
    # Класс для яиц
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("data/newEgg1.png")
        self.name = 'newEgg.png'
        self.rect = self.image.get_rect()
        self.rect.x = False
        self.rect.y = False
        self.all_positions = {
            'left_up': [(60, 120), (90, 140), (120, 160), (120, 160)],
            'left_down': [(60, 260), (90, 275), (120, 290), (120, 290)],
            'right_up': [(520, 120), (495, 135), (460, 160), (460, 160)],
            'right_down': [(520, 260), (495, 270), (460, 290), (460, 290)]
        }
        self.position = random.choice(['left_up', 'right_up', 'left_down', 'right_down'])
        self.coords = self.all_positions[self.position]
        self.index = 0
        self.is_caught = False

    def choose_position(self):
        # Обозначение позиции яйца
        self.coords = self.all_positions[self.position]

    def update(self):
        # Обновление координат яйца
        crd = self.coords[self.index]
        self.rect.x = crd[0]
        self.rect.y = crd[1]

    def update_index(self):
        # Обновление индекса яйца
        self.index += 1

    def draw(self, screen):
        # Отрисовка яйца на экране
        if self.rect.x and self.rect.y:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def rotate(self):
        # Переворот яйца
        if self.index != 0:
            fullname = os.path.join('data', self.name)
            im = Image.open(fullname)
            im = im.rotate(90, expand=True)
            im.save('data/newEgg.png')
            self.image = pygame.image.load("data/newEgg.png")

    def catch(self, arms_pos):
        # Проверка на то, было ли поймано яйцо
        if self.position == arms_pos:
            return True
