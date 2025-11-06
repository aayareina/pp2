import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))   # окно
clock = pygame.time.Clock()                    # контроль fps

radius = 6      # размер кисти
mode = "blue"   # текущий цвет
points = []     # список точек для рисования следа

# функция для рисования плавной линии между точками
def draw_line(screen, start, end, w, mode, index):
    c1 = max(0, min(255, 2 * index - 256))   # плавное изменение цвета
    c2 = max(0, min(255, 2 * index))

    # выбор цвета
    if mode == "blue":
        color = (c1, c1, c2)
    elif mode == "red":
        color = (c2, c1, c1)
    else:
        color = (c1, c2, c1)

    dx = end[0] - start[0]   # разница по x
    dy = end[1] - start[1]   # разница по y

    steps = max(abs(dx), abs(dy))  # количество шагов для плавности
    if steps == 0:
        return

    # интерполяция для плавной линии
    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)
        pygame.draw.circle(screen, color, (x, y), w)  # маленькие круги


running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:   # выход
            running = False

        if e.type == pygame.KEYDOWN:    # смена цвета
            if e.key == pygame.K_ESCAPE:
                running = False
            if e.key == pygame.K_r:
                mode = "red"
            if e.key == pygame.K_g:
                mode = "green"
            if e.key == pygame.K_b:
                mode = "blue"

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:   # увеличивает кисть
                radius = min(200, radius + 1)
            if e.button == 3:   # уменьшает кисть
                radius = max(1, radius - 1)

        if e.type == pygame.MOUSEMOTION:  # добавление новой точки
            points.append(e.pos)
            points = points[-256:]       # ограничивание хвоста

    screen.fill((0, 0, 0))  # чистка экрана

    #линии между точками
    for i in range(len(points) - 1):
        draw_line(screen, points[i], points[i + 1], radius, mode, i)

    pygame.display.flip()   
    clock.tick(60)          # fps

pygame.quit()
