import pygame
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

win_windt = 500
win_height = 500
win = pygame.display.set_mode((win_windt, win_height))

pygame.display.set_caption("Header window")

# Настройки персонажа
x = 50
y = 50
width = 50
height = 50
speed = 5

isJump = False
jump = 10

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Совержения действий
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < (win_windt - width - 5):
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < (win_height - height - 5):
        y += speed

    # Закрашиваем окно
    win.fill((0, 0, 0))
    # Рисуем персонажа
    # Окно \ Цвет \ Положение,Размеры
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()