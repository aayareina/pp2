import pygame
import random
from connectS import conn, cur


username = input("Введите имя: ")


cur.execute("SELECT id FROM users WHERE username=%s", (username,))
u = cur.fetchone()

if u:
    user_id = u[0]
else:
    cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()


cur.execute("SELECT level FROM user_score WHERE user_id=%s ORDER BY id DESC LIMIT 1", (user_id,))
row = cur.fetchone()

if row:
    level = row[0]
else:
    level = 1

print("Ваш уровень:", level)

pygame.init()
w = 400
h = 400
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

x = 200
y = 200
dx = 20
dy = 0

food_x = random.randrange(0, w, 20)
food_y = random.randrange(0, h, 20)
score = 0

run = True

while run:

    pygame.time.delay(100)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                dx = -20
                dy = 0
            if i.key == pygame.K_RIGHT:
                dx = 20
                dy = 0
            if i.key == pygame.K_UP:
                dy = -20
                dx = 0
            if i.key == pygame.K_DOWN:
                dy = 20
                dx = 0
            if i.key == pygame.K_p:  # P = pause/save
                cur.execute("INSERT INTO user_score(user_id, level, score) VALUES(%s, %s, %s)",
                            (user_id, level, score))
                conn.commit()
                print("Сохранено")

    x += dx
    y += dy

  
    if x == food_x and y == food_y:
        score += 1
        food_x = random.randrange(0, w, 20)
        food_y = random.randrange(0, h, 20)
        if score % 3 == 0:
            level += 1


    if x < 0 or x > w - 20 or y < 0 or y > h - 20:
        run = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, 20, 20))
    pygame.draw.rect(win, (255, 0, 0), (food_x, food_y, 20, 20))
    pygame.display.update()

pygame.quit()

cur.close()
conn.close()
