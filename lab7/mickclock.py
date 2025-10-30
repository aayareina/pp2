import pygame
import math
import datetime

pygame.init()


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(" KUROMI 🌸 Clock 🕰")


black = (0, 0, 0)
center = (250, 250)


bg = pygame.image.load("kuromi.jpeg")
bg = pygame.transform.scale(bg, (500, 500))


def draw_arrow(surface, color, start, end, width):
    pygame.draw.line(surface, color, start, end, width)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)
    size = 10
    points = [
        (end[0], end[1]),
        (end[0] - size * math.cos(angle - 0.3), end[1] - size * math.sin(angle - 0.3)),
        (end[0] - size * math.cos(angle + 0.3), end[1] - size * math.sin(angle + 0.3))
    ]
    pygame.draw.polygon(surface, color, points)


running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg, (0, 0))

    
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    
    min_angle = math.radians((minute + second / 60) * 6 - 90)
    sec_angle = math.radians(second * 6 - 90)

    
    min_end = (center[0] + math.cos(min_angle) * 120, center[1] + math.sin(min_angle) * 120)
    sec_end = (center[0] + math.cos(sec_angle) * 170, center[1] + math.sin(sec_angle) * 170)

    
    draw_arrow(screen, black, center, min_end, 7)
    draw_arrow(screen, black, center, sec_end, 4)

    
    pygame.draw.circle(screen, black, center, 8)

    pygame.display.update()
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
