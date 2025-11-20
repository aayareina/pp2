import pygame
import sys
import random
from pygame.locals import *

pygame.init()

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
yellow = pygame.Color(255, 255, 0)

screen_width = 400
screen_height = 600
displaysurf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RACER")
font = pygame.font.SysFont("Verdana", 60)

fps = pygame.time.Clock()

# новые переменные 
enemy_speed = 10
speed_up_every = 5   # каждые 5 монет ускорение


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, enemy_speed)
        if self.rect.bottom > screen_height:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 300), 0)    
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # вес монеты (маленькие переменные)
        self.weight = random.choice([1, 2, 3])
        size = 12 * self.weight

        self.image = pygame.Surface((size, size))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 60), random.randint(0, 400))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > screen_height:
            self.reset()

    def reset(self):
        self.weight = random.choice([1, 2, 3])
        size = 12 * self.weight
        self.image = pygame.Surface((size, size))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


p1 = Player()
e1 = Enemy()
c1 = Coin()


score = 0
font2 = pygame.font.SysFont("Courier New", 20)
game_over = False



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        p1.update()
        e1.move()
        c1.move()

    # сбор монет
    if p1.rect.colliderect(c1.rect):
        score += c1.weight
        if score % speed_up_every == 0:
            enemy_speed += 2
        c1.reset()
    
    # столкновение с врагом
    if p1.rect.colliderect(e1.rect):
        game_over = True
        
    displaysurf.fill(white)
    pygame.draw.rect(displaysurf, grey, (50, 0, 300, 600))

    p1.draw(displaysurf)
    e1.draw(displaysurf)
    c1.draw(displaysurf)

    text = font2.render(f"Coins: {score}", True, black)
    displaysurf.blit(text, (10, 10))
            
    if game_over:
        displaysurf.blit(font.render("GAME OVER", True, black), (30, 250))

    pygame.display.update()
    fps.tick(60)
