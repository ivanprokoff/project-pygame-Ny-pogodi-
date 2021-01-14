import pygame
import sys

from loading import load_image

from miss import Miss
from wolf import Wolf
from egg import Egg
from arms import Arms
from chickens import Chickens


FPS = 50
WIDTH = 600
HEIGHT = 450
ONE_STEP = 1700

arms_positions = {
        'left_down': 'armDownLeft.png',
        'left_up': 'armUpLeft.png',
        'right_down': 'armDownRight.png',
        'right_up': 'armUpRight.png'
    }

body_pos = 'left'
arms_pos = 'left_down'

time = 0
counter = 0
misses = 0
interval = 0


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    # стартовый экран игры
    sound = pygame.mixer.Sound('data/music.wav')
    sound.play()
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
                screen.fill(pygame.Color('white'))
                background = pygame.transform.scale(load_image('background.png'), (WIDTH, HEIGHT))
                screen.blit(background, (0, 0))
                screen.blit(arms.image, (0, 0))
                sound.stop()
                return
        pygame.display.flip()
        clock.tick(FPS)


def spawn_egg():
    # Функция генерации яйца
    eggs.append(Egg())


def render():
    # Функция отрисовки сцены
    screen.blit(background, (0, 0))
    wolf_sprite.draw(screen)
    all_sprites.draw(screen)
    misses_sprites.draw(screen)
    screen.blit(arms.image, (0, 0))


def game_over():
    # завершение игры
    global running
    background = pygame.transform.scale(load_image('game_over.png'), (WIDTH, HEIGHT))
    running = False
    run = True
    x = -500
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(background, (x, 0))
        x += 10
        pygame.display.flip()
        clock.tick(FPS)
        if x == 0:
            run = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(background, (10, 0))


def miss():
    # функция вызывается при пропуске яйца
    global misses
    Miss(misses_sprites)
    misses_sprites.update()
    misses += 1
    print('промах')
    print(misses)
    if misses == 3:
        Miss(misses_sprites)
        misses_sprites.update()
        clock.tick(FPS)
        game_over()


if __name__ == '__main__':
    pygame.init()
    start = True
    running = True

    pygame.display.set_caption('Ну, погоди! | Помоги волку собрать яйца')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()

    background = pygame.transform.scale(load_image('background.png'), (WIDTH, HEIGHT))
    wolf_left = load_image('wolf_main_left.png')
    wolf_right = load_image('wolf_main_right.png')

    wolf_sprite = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    misses_sprites = pygame.sprite.Group()

    Wolf(wolf_sprite)
    Chickens(all_sprites)
    arms = Arms()

    eggs = []

    screen.blit(arms.image, (0, 0))

    while running:
        # Главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if start:
                # Вызов стартового экрана
                start_screen()
                start = False
            if event.type == pygame.KEYDOWN:
                # Обработка событий - нажатия стрелок
                if event.key == pygame.K_RIGHT:
                    body_pos = 'right'
                    arms_pos = arms.update_arms('right', arms_pos, body_pos)
                    wolf_sprite.update('right')
                    screen.blit(arms.image, (0, 0))
                if event.key == pygame.K_LEFT:
                    body_pos = 'left'
                    arms_pos = arms.update_arms('left', arms_pos, body_pos)
                    wolf_sprite.update('left')
                    screen.blit(arms.image, (0, 0))
                if event.key == pygame.K_UP:
                    arms_pos = arms.update_arms('up', arms_pos, body_pos)
                if event.key == pygame.K_DOWN:
                    arms_pos = arms.update_arms('down', arms_pos, body_pos)

        render()

        if running:
            # Обработка яиц
            time += clock.get_time()
            if time > ONE_STEP:
                time = 0
                shift = False
                for egg in eggs:
                    egg.update()
                    egg.update_index()
                    if egg.index != 0:
                        egg.rotate()
                    if egg.index == 4:
                        if egg.catch(arms_pos):
                            counter += 1
                        else:
                            miss()
                        eggs.remove(egg)
                if interval % 2 == 0:
                    shift = True
                if shift:
                    spawn_egg()
                    shift = False
                interval += 1
            for egg in eggs:
                # Отрисовка яиц
                egg.draw(screen)
            if counter == 20:
                # Если набираем 20 яиц, ускоряем игру
                ONE_STEP = ONE_STEP - 2
            text1 = font.render(str(counter), True,
                              (51, 51, 255))
            screen.blit(text1, (120, 20))
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
