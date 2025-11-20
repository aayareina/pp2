import pygame, random

pygame.init()

# окно
w, h = 600, 600
cell = 20
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

# змейка
snake = [(5, 5)]
direction = (1, 0)
score = 0
level = 1
speed = 7

# еда с весом и таймером
fw = 1        # вес еды
ft = 0        # таймер еды
ft_max = 180  # исчезает через 180 кадров (3 сек)

# препятствия
walls = []  # список стен

def new_food():
    # генерация еды
    global fw, ft
    while True:
        x = random.randint(0, (w // cell) - 1)
        y = random.randint(0, (h // cell) - 1)
        if (x, y) not in snake and (x, y) not in walls:
            fw = random.randint(1, 3)
            ft = ft_max
            return (x, y)

def new_walls(lv):
    # новые препятствия с уровнем
    walls.clear()
    for _ in range(lv + 2):  # число стен растёт с уровнем
        while True:
            x = random.randint(0, (w // cell) - 1)
            y = random.randint(0, (h // cell) - 1)
            if (x, y) not in snake:
                walls.append((x, y))
                break

food = new_food()
new_walls(level)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        # управление
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            if e.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            if e.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            if e.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # движение змейки
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # проверка границ
    if new_head[0] < 0 or new_head[0] >= w // cell or new_head[1] < 0 or new_head[1] >= h // cell:
        running = False

    # столкновение с собой
    if new_head in snake:
        running = False

    # столкновение со стеной
    if new_head in walls:
        running = False

    snake.insert(0, new_head)

    # еда исчезает по таймеру
    ft -= 1
    if ft <= 0:
        food = new_food()

    # поедание еды
    if new_head == food:
        score += fw

        # каждые 4 очка → уровень ↑, скорость ↑, добавляем стены
        if score % 4 == 0:
            level += 1
            speed += 2
            new_walls(level)

        food = new_food()
    else:
        snake.pop()

    # отрисовка
    screen.fill((0, 0, 0))

    # яблоко
    col = (255, 120, 50) if fw == 1 else (255, 200, 40) if fw == 2 else (255, 60, 60)
    pygame.draw.rect(screen, col, (food[0]*cell, food[1]*cell, cell, cell))

    # змейка
    for (x, y) in snake:
        pygame.draw.rect(screen, (180, 70, 255), (x*cell, y*cell, cell, cell))

    # стены
    for (x, y) in walls:
        pygame.draw.rect(screen, (100, 100, 100), (x*cell, y*cell, cell, cell))

    # текст
    font = pygame.font.SysFont("Arial", 22)
    txt = font.render(f"Score: {score}  Level: {level}  Food:{fw}", True, (255, 255, 255))
    screen.blit(txt, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
