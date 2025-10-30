import pygame

pygame.init()


WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎈")


WHITE = (255, 255, 255)
PURPLE = (128, 0, 128) 


radius = 25
x = WIDTH // 2
y = HEIGHT // 2


speed = 20

run = True
while run:
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, PURPLE, (x, y), radius)
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= HEIGHT:
        y += speed
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= WIDTH:
        x += speed

pygame.quit()
