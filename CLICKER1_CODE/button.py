class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def DRAW_ON_SCREEN(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def rect_button(self, image):
        rect = image.get_rect(topleft=(self.x, self.y))
        return rect