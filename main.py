import pygame
import sys
import os
from loading import load_image
from chickens import Chickens


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Нажмите любую клавишу',
                  'для продолжения']

    fon = pygame.transform.scale(load_image('fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                print('поихали')
                screen.fill(pygame.Color('white'))
                background = pygame.transform.scale(load_image('background.png'), (width, height))
                screen.blit(background, (0, 0))
                return
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    start = True
    pygame.display.set_caption('Ну, погоди! | Помоги волку собрать яйца')
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    background = load_image('background.png')
    wolf = load_image('wolf_main_left.png')
    chickens = load_image('chickens.png')
    all_sprites = pygame.sprite.Group()
    Chickens(all_sprites)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif start:
                start_screen()
                start = False
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
