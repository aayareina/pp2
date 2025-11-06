import pygame
import sys
import random
from pygame.locals import *

pygame.init()

Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Grey = pygame.Color(128, 128, 128)
Purple = pygame.Color(128, 0, 128)
Blue = pygame.Color(0, 0, 255)
Yellow = pygame.Color(255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("RACER")

FPS = pygame.time.Clock()
  
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image,(70, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
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
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(Yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 60),random.randint(0, 400))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  

P1 = Player()
E1 = Enemy()
C1 = Coin()

score = 0
font = pygame.font.SysFont("Courier New", 20)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    C1.move()

    if P1.rect.colliderect(C1.rect):
        score += 1
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    DISPLAYSURF.fill(White)
    pygame.draw.rect(DISPLAYSURF, Grey, (50, 0, 300, 600))
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    text = font.render(f"Coins: {score}", True, Black)
    DISPLAYSURF.blit(text, (10, 10))

    pygame.display.update()
    FPS.tick(60)
