import pygame
import os
import sys

pygame.init()
pygame.mixer.init()


W = 500
H = 500
bg_color = (30, 30, 30)
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Music Player")


folder = "music"
song_list = [f for f in os.listdir(folder) if f.endswith(".mp3")]

if len(song_list) == 0:
    print("No songs found in the folder!!")
    sys.exit()


current_song = 0
pygame.mixer.music.load(os.path.join(folder, song_list[current_song]))


try:
    picture = pygame.image.load("cover.jpeg")
    picture = pygame.transform.scale(picture, (270, 270))
except:
    picture = None


try:
    btn_prev = pygame.image.load("prev.jpeg")
    btn_play = pygame.image.load("play.jpeg")
    btn_next = pygame.image.load("next.jpeg")
    btn_prev = pygame.transform.scale(btn_prev, (60, 60))
    btn_play = pygame.transform.scale(btn_play, (60, 60))
    btn_next = pygame.transform.scale(btn_next, (60, 60))
except:
    print("No button images found!")
    sys.exit()


rect_prev = pygame.Rect(W//2 - 150, H - 100, 60, 60)
rect_play = pygame.Rect(W//2 - 30, H - 100, 60, 60)
rect_next = pygame.Rect(W//2 + 90, H - 100, 60, 60)


playing = False
paused = False

def draw_screen():
    window.fill(bg_color)
    if picture:
        window.blit(picture, (W//2 - 135, 60))
    window.blit(btn_prev, rect_prev.topleft)
    window.blit(btn_play, rect_play.topleft)
    window.blit(btn_next, rect_next.topleft)

    font = pygame.font.SysFont("arial", 22)
    text = font.render(song_list[current_song], True, (255, 255, 255))
    window.blit(text, (W//2 - text.get_width()//2, H - 150))

    pygame.display.update()


def start_song():
    global playing, paused
    pygame.mixer.music.play()
    playing = True
    paused = False


def play_pause():
    global playing, paused
    if not playing:
        start_song()
    elif paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def next_song():
    global current_song
    current_song = (current_song + 1) % len(song_list)
    pygame.mixer.music.load(os.path.join(folder, song_list[current_song]))
    start_song()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(song_list)
    pygame.mixer.music.load(os.path.join(folder, song_list[current_song]))
    start_song()


running = True
draw_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause()
            if event.key == pygame.K_RIGHT:
                next_song()
            if event.key == pygame.K_LEFT:
                prev_song()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_prev.collidepoint(event.pos):
                prev_song()
            if rect_play.collidepoint(event.pos):
                play_pause()
            if rect_next.collidepoint(event.pos):
                next_song()

    draw_screen()

pygame.quit()
sys.exit()
