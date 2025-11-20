import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

radius = 6
mode = "blue"
points = []

#режим для фигур
shape = None  # s - square, t - triangle, e - equilateral, d - diamond

#функция  плавной линии
def draw_line(screen, start, end, w, mode, index):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if mode == "blue":
        color = (c1, c1, c2)
    elif mode == "red":
        color = (c2, c1, c1)
    else:
        color = (c1, c2, c1)

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return

    for i in range(steps):
        t = i / steps
        x = int(start[0] * (1 - t) + end[0] * t)
        y = int(start[1] * (1 - t) + end[1] * t)
        pygame.draw.circle(screen, color, (x, y), w)


# фигуры
def draw_square(x, y, s):
    pygame.draw.rect(screen, (200, 200, 200), (x - s//2, y - s//2, s, s), 2)

def draw_rtriangle(x, y, s):
    p1 = (x - s//2, y + s//2)
    p2 = (x + s//2, y + s//2)
    p3 = (x - s//2, y - s//2)
    pygame.draw.polygon(screen, (200, 200, 200), [p1, p2, p3], 2)

def draw_eqtriangle(x, y, s):
    h = (3**0.5 / 2) * s
    p1 = (x - s//2, y + int(h/2))
    p2 = (x + s//2, y + int(h/2))
    p3 = (x, y - int(h/2))
    pygame.draw.polygon(screen, (200, 200, 200), [p1, p2, p3], 2)

def draw_rhombus(x, y, s):
    p1 = (x, y - s//2)
    p2 = (x + s//2, y)
    p3 = (x, y + s//2)
    p4 = (x - s//2, y)
    pygame.draw.polygon(screen, (200, 200, 200), [p1, p2, p3, p4], 2)


# цикл
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

            # смена цвета
            if e.key == pygame.K_r:
                mode = "red"
            if e.key == pygame.K_g:
                mode = "green"
            if e.key == pygame.K_b:
                mode = "blue"

            # выбор фигуры
            if e.key == pygame.K_s:
                shape = "square"
            if e.key == pygame.K_t:
                shape = "tri"
            if e.key == pygame.K_e:
                shape = "eq"
            if e.key == pygame.K_d:
                shape = "rh"

        #увеличение/уменьшение кисти
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                radius = min(200, radius + 1)
            if e.button == 3:
                radius = max(1, radius - 1)

        #рисование линии и фигур
        if e.type == pygame.MOUSEMOTION:
            points.append(e.pos)
            points = points[-256:]

            mx, my = e.pos
            if shape == "square":
                draw_square(mx, my, 80)
            elif shape == "tri":
                draw_rtriangle(mx, my, 80)
            elif shape == "eq":
                draw_eqtriangle(mx, my, 80)
            elif shape == "rh":
                draw_rhombus(mx, my, 80)

    screen.fill((0, 0, 0))

    for i in range(len(points) - 1):
        draw_line(screen, points[i], points[i + 1], radius, mode, i)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
