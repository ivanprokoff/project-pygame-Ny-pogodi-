import pygame
from loading import load_image


class Arms():
    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        self.image = load_image("armDownLeft.png")
        self.rect = self.image.get_rect()
        self.arms_positions = {
            'left_down': 'armDownLeft.png',
            'left_up': 'armUpLeft.png',
            'right_down': 'armDownRight.png',
            'right_up': 'armUpRight.png'
        }
        self.mask = pygame.mask.from_surface(self.image)

    def update_arms(self, side, arms_pos, body_pos, screen):
        if side == 'right' and arms_pos == 'left_down':
            self.image = load_image(self.arms_positions['right_down'])
            return 'right_down'

        elif side == 'up' and body_pos == 'left':
            self.image = load_image(self.arms_positions['left_up'])
            print('обновление рук')
            return 'left_up'

        elif side == 'up' and body_pos == 'right':
            self.image = load_image(self.arms_positions['right_up'])
            return 'right_up'

        elif side == 'left' and arms_pos == 'right_down':
            self.image = load_image(self.arms_positions['left_down'])
            return 'left_down'

        elif side == 'left' and arms_pos == 'right_up':
            self.image = load_image(self.arms_positions['left_up'])
            return 'left_up'

        elif side == 'right' and arms_pos == 'left_up':
            self.image = load_image(self.arms_positions['right_up'])
            return 'right_up'

        elif side == 'down' and body_pos == 'right':
            self.image = load_image(self.arms_positions['right_down'])
            return 'right_down'

        elif side == 'down' and body_pos == 'left':
            self.image = load_image(self.arms_positions['left_down'])
            return 'left_down'
