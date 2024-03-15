import pygame

class Texts:
    def __init__(self, font, text, size, x, y, color):
        self.font = pygame.font.Font(font, size)
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.rendered_text = self.font.render(self.text, False, self.color)
        self.rect = self.rendered_text.get_rect(topleft=(self.x, self.y))

    def render_texts(self, screen):
        screen.blit(self.rendered_text, self.rect)
