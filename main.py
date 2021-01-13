import pygame
import sys
import os
from loading import load_image
from chickens import Chickens
from wolf import Wolf
from egg import Egg
from arms import Arms


FPS = 50
WIDTH = 600
HEIGHT = 450


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Нажмите любую клавишу',
                  'для продолжения']

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
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
                background = pygame.transform.scale(load_image('background.png'), (WIDTH, HEIGHT))
                screen.blit(background, (0, 0))
                screen.blit(arms.image, (0, 0))
                return
        pygame.display.flip()
        clock.tick(FPS)


def spawn_egg():
    eggs.append(Egg())


if __name__ == '__main__':
    pygame.init()
    start = True
    pygame.display.set_caption('Ну, погоди! | Помоги волку собрать яйца')
    arms_positions = {
        'left_down': 'armDownLeft.png',
        'left_up': 'armUpLeft.png',
        'right_down': 'armDownRight.png',
        'right_up': 'armUpRight.png'
    }
    TIME_PER_STEP = 1500
    body_pos = 'left'
    arms_pos = 'left_down'
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    running = True
    time = 0
    clock = pygame.time.Clock()
    background = pygame.transform.scale(load_image('background.png'), (WIDTH, HEIGHT))
    wolf_left = load_image('wolf_main_left.png')
    wolf_right = load_image('wolf_main_right.png')
    wolf_sprite = pygame.sprite.Group()
    Wolf(wolf_sprite)
    all_sprites = pygame.sprite.Group()
    eggs = []
    Chickens(all_sprites)
    arms = Arms()
    screen.blit(arms.image, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if start:
                start_screen()
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    body_pos = 'right'
                    arms_pos = arms.update_arms('right', arms_pos, body_pos, screen)
                    wolf_sprite.update('right')
                    screen.blit(arms.image, (0, 0))
                if event.key == pygame.K_LEFT:
                    body_pos = 'left'
                    arms_pos = arms.update_arms('left', arms_pos, body_pos, screen)
                    wolf_sprite.update('left')
                    screen.blit(arms.image, (0, 0))
                if event.key == pygame.K_UP:
                    arms_pos = arms.update_arms('up', arms_pos, body_pos, screen)
                if event.key == pygame.K_DOWN:
                    arms_pos = arms.update_arms('down', arms_pos, body_pos, screen)
        screen.blit(background, (0, 0))
        wolf_sprite.draw(screen)
        all_sprites.draw(screen)
        screen.blit(arms.image, (0, 0))
        if running:
            time += clock.get_time()
        if time > TIME_PER_STEP:
            time = 0
            shift = False
            for egg in eggs:
                egg.update(screen)
                egg.update_index()
                if egg.index > 2:
                    eggs.remove(egg)
                    print('яйцо удалено')
            spawn_egg()
            print('яйцо создано')
        for egg in eggs:
            egg.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
