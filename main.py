import pygame
import sys
import os
from loading import load_image
from chickens import Chickens
from wolf import Wolf
from egg import Egg


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


def update_arms(side):
    global arms_pos
    if side == 'right' and arms_pos == 'left_down':
        arms = load_image(arms_positions['right_down'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'right_down'

    elif side == 'up' and body_pos == 'left':
        arms = load_image(arms_positions['left_up'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'left_up'

    elif side == 'up' and body_pos == 'right':
        arms = load_image(arms_positions['right_up'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'right_up'

    elif side == 'left' and arms_pos == 'right_down':
        arms = load_image(arms_positions['left_down'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'left_down'

    elif side == 'left' and arms_pos == 'right_up':
        arms = load_image(arms_positions['left_up'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'left_up'

    elif side == 'right' and arms_pos == 'left_up':
        arms = load_image(arms_positions['right_up'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'right_up'

    elif side == 'down' and body_pos == 'right':
        arms = load_image(arms_positions['right_down'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'right_down'

    elif side == 'down' and body_pos == 'left':
        arms = load_image(arms_positions['left_down'])
        screen.blit(background, (0, 0))
        screen.blit(arms, (0, 0))
        arms_pos = 'left_down'
    else:
        pass


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
    size = width, height = 600, 450
    screen = pygame.display.set_mode(size)
    running = True
    time = 0
    clock = pygame.time.Clock()
    background = pygame.transform.scale(load_image('background.png'), (width, height))
    wolf_left = load_image('wolf_main_left.png')
    wolf_right = load_image('wolf_main_right.png')
    wolf_sprite = pygame.sprite.Group()
    Wolf(wolf_sprite)
    all_sprites = pygame.sprite.Group()
    eggs = []
    Chickens(all_sprites)
    arms = load_image('armDownLeft.png')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if start:
                start_screen()
                start = False
                screen.blit(arms, (0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    body_pos = 'right'
                    update_arms('right')
                    wolf_sprite.update('right')
                if event.key == pygame.K_LEFT:
                    body_pos = 'left'
                    update_arms('left')
                    wolf_sprite.update('left')
                if event.key == pygame.K_UP:
                    update_arms('up')
                if event.key == pygame.K_DOWN:
                    update_arms('down')
        spawn_egg()
        for egg in eggs:
            if egg.index == 3:
                eggs.remove(egg)
            egg.choose_position()
            egg.draw(screen)
            egg.update(screen)
        wolf_sprite.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
