import pygame
import sys

# Инициализация Pygame
pygame.init()

# Задание размера игрового поля
game_width = 500
game_height = 500

# Создание игрового окна
game_display = pygame.display.set_mode((game_width, game_height))

# Установка заголовка окна
pygame.display.set_caption('My Game')

# Цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Получение позиции мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Нормализация позиции мыши
    normalized_x = mouse_x / (game_width - 1)
    normalized_y = mouse_y / (game_height - 1)

    # Вычисление цвета фона
    red = min(int(normalized_x * 255) + 40, 255)
    green = min(int((normalized_x + normalized_y) * 255 / 5) + 10 , 255)
    blue = min(int(normalized_y * 255) + 10, 255)
    bg_color = (red, green, blue)

    # Отрисовка фона
    game_display.fill(bg_color)

    # Обновление экрана
    pygame.display.update()
