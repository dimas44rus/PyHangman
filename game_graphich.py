import pygame
import game_core
import words_operations
import random

# Инициализируем PyGame
pygame.init()

# Устанавливаем размер окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Устанавливаем заголовок окна
pygame.display.set_caption("Виселица")

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определяем шрифт
font = pygame.font.Font(None, 36)

# Определяем пункты меню
menu_items = ["Играть","Выход"]
# Определяем текущий пункт меню
current_item = 0

# Главный цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_item = (current_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                current_item = (current_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if current_item == 0:
                    # Новая игра
                    print("Новая игра")
                    # Здесь можно запустить новую игру
                elif current_item == 1:
                    # Загрузить игру
                    print("Загрузить игру")
                    # Здесь можно загрузить сохраненную игру
                elif current_item == 2:
                    # Инструкция
                    print("Инструкция")
                    # Здесь можно отобразить инструкцию к игре
                elif current_item == 3:
                    # Выход
                    pygame.quit()
                    sys.exit()

    # Очищаем экран
    screen.fill(BLACK)

    # Рисуем пункты меню
    for i, item in enumerate(menu_items):
        color = WHITE if i == current_item else (200, 200, 200)
        text = font.render(item, True, color)
        screen.blit(text, (100, 100 + i * 50))

    # Обновляем экран
    pygame.display.flip()





