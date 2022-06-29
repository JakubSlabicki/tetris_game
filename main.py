import pygame
import sys
from random import randint
from pygame.locals import *
from TetrominosFigure import TetrominossFigure
from TetrominosMap import TetrominosMap

# CONST VARIABLE
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_NAME = 'Tetris Game'
WINDOW_IMAGE_PATH = r'.\files\background.png'
WINDOW_FONT = 'Comic Sans MS'
WINDOW_FONT_SIZE = 50
WINDOW_CYCLE_MS = 10
WINDOW_SCORE_X = 1065
WINDOW_SCORE_Y = 65
COLOR_RGB_BLACK = (0, 0, 0)

# Create Widndow Display and Font
window_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
image = pygame.image.load(WINDOW_IMAGE_PATH)
pygame.display.set_caption(WINDOW_NAME)
pygame.init()
pygame.font.init()
window_font = pygame.font.SysFont(WINDOW_FONT, WINDOW_FONT_SIZE)

# Create Global Map
global_map = TetrominosMap()

# Create first Tetriminoss Figures
tetro = TetrominossFigure(ini_map=global_map)
next_tetro = TetrominossFigure(ini_map=global_map, start_x=810, start_y=85, ini_type=randint(1, 5))

# Main game loop
while True:
    # 1. Upload Widnow image and points
    window_display.blit(image, (0, 0))
    window_display.blit(window_font.render(str(global_map.score), False, COLOR_RGB_BLACK),

                        (WINDOW_SCORE_X, WINDOW_SCORE_Y))

    # 2.Create new Tetriminoss Figures or draw existing ones with updated posiotions
    if tetro.mapped:
        tetro = TetrominossFigure(ini_map=global_map, ini_type=next_tetro.type)
        next_tetro = TetrominossFigure(ini_map=global_map, start_x=810, start_y=85, ini_type=randint(1, 5))
    else:
        tetro.draw(window_display)
        next_tetro.draw(window_display)

    # 3. Draw mapped Tetriminoss Figures
    global_map.draw_map(window_display)

    # Update Widnow Display with
    # 1. Image and score
    # 2. Tetriminoss Figures
    # 3. Map
    pygame.display.update()

    # Check pressed keyboard keys
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tetro.update_x_angle_pos(0, 1)
            if event.key == pygame.K_DOWN:
                tetro.update_x_angle_pos(0, -1)
            if event.key == pygame.K_RIGHT:
                tetro.update_x_angle_pos(1, 0)
            if event.key == pygame.K_LEFT:
                tetro.update_x_angle_pos(-1, 0)
        if pygame.key.get_pressed()[K_SPACE]:
            global_map.step += 10

    # Wait and udpate Y position
    pygame.time.wait(WINDOW_CYCLE_MS)
    if global_map.step >= 10:
        tetro.update_y_pos()
        global_map.step = 0

    # Increment step by actual udpate speed
    global_map.step += global_map.update_speed

