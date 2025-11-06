import pygame, random

pygame.init()

# окно
w, h = 600, 600
cell = 20
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

# змейка
snake = [(5, 5)]
direction = (1, 0)  # движение вправо
score = 0
level = 1
speed = 7

# еда (функция чтобы не появлялась на змейке)
def new_food():
    while True:
        x = random.randint(0, (w // cell) - 1)
        y = random.randint(0, (h // cell) - 1)
        if (x, y) not in snake:
            return (x, y)

food = new_food()

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

    # проверка выхода за границы → проигрыш
    if new_head[0] < 0 or new_head[0] >= w // cell or new_head[1] < 0 or new_head[1] >= h // cell:
        running = False

    # проверка столкновения с собой → проигрыш
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # еда
    if new_head == food:
        score += 1
        
        # каждые 4 еды → уровень + скорость ↑
        if score % 4 == 0:
            level += 1
            speed += 2
        
        food = new_food()
    else:
        snake.pop()

    # отрисовка
    screen.fill((0, 0, 0))

    #яблоко
    pygame.draw.rect(screen, (255, 100, 200), (food[0]*cell, food[1]*cell, cell, cell))

    #змейка
    for (x, y) in snake:
        pygame.draw.rect(screen, (180, 70, 255), (x*cell, y*cell, cell, cell))

    # текст
    font = pygame.font.SysFont("Arial", 22)
    txt = font.render(f"Score: {score}   Level: {level}", True, (255, 255, 255))
    screen.blit(txt, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
