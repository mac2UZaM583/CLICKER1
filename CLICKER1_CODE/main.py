import pygame
from texts import Texts
from button import Button
from shake import Shake

# PYGAME INIT --------------------------- #
pygame.init()
pygame.mixer.init()
clock1 = pygame.time.Clock()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CLICKER1")
pygame.display.set_icon(pygame.image.load('images/icon.png'))

FPS = 60
score = 0
sound_1_playing = True

# GET DATA --------------------------- #
button_image_1_1 = pygame.image.load('images/button_1(1).png')
button_image_1_2 = pygame.image.load('images/button_1(2).png')
button_width = button_image_1_1.get_width()
button_height = button_image_1_1.get_height()
center_button_x = (screen_width - button_width) // 2
center_button_y = (screen_height - button_height) // 2
button_1_1 = Button(button_image_1_1, center_button_x, center_button_y)

font1 = 'fonts/pixel-anchor-jack_0.ttf'
text1 = str(score)
text1_size = 20
text1_x = screen_width // 2
text1_y = 50
text1_color = (255, 255, 255)
text1_surface = Texts(font1, text1, text1_size, 0, text1_y, text1_color)
text1_x = (screen.get_width() - text1_surface.rendered_text.get_width()) // 2
text1_surface = Texts(font1, text1, text1_size, text1_x, text1_y, text1_color)

shake = Shake(text1_x, text1_y, 10)

sound_1 = pygame.mixer.Sound("sounds/sound_1.ogg")
pygame.mixer.music.load("sounds/Неизвестен - Без названия.mp3")
pygame.mixer.music.queue("sounds/Неизвестен - Без названия_2.mp3")
pygame.mixer.music.play()

# GAME INIT --------------------------- #
run = True

while run:

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("sounds/Неизвестен - Без названия.mp3")
        pygame.mixer.music.queue("sounds/Неизвестен - Без названия_2.mp3")
        pygame.mixer.music.play()

    # SET DATA --------------------------- #
    clock1.tick(FPS)

    screen.fill((200, 0, 0))
    button_1_1.DRAW_ON_SCREEN(screen)
    text1_surface.render_texts(screen)

    mouse_position = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] and button_1_1.rect_button(button_image_1_1).collidepoint(mouse_position) and sound_1_playing:
        button_1_1 = Button(button_image_1_2, center_button_x, center_button_y)

        score += 1
        text1 = str(score)

        text1_surface = Texts(font1, text1, text1_size, 0, text1_y, text1_color)
        text1_x = (screen.get_width() - text1_surface.rendered_text.get_width()) // 2
        text1_surface = Texts(font1, text1, text1_size, shake.shake_x(text1_x), shake.shake_y(text1_y), text1_color)

        sound_1.play()
        sound_1_playing = False

    elif not pygame.mouse.get_pressed()[0]:
        button_1_1 = Button(button_image_1_1, center_button_x, center_button_y)

        text1_surface = Texts(font1, text1, text1_size, 0, text1_y, text1_color)
        text1_x = (screen.get_width() - text1_surface.rendered_text.get_width()) // 2
        text1_surface = Texts(font1, text1, text1_size, text1_x, text1_y, text1_color)

        sound_1_playing = True


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
