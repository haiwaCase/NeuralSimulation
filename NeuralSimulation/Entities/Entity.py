import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, position, happiness, sprite):
        super().__init__()
        self.position = position
        self.happiness = happiness
        self.zoom_size = 1
        self.image = pygame.image.load(sprite)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def set_position_x(self, x):
        self.position.set_x(x)

    def set_position_y(self, y):
        self.position.set_y(y)

    def get_happiness(self):
        return self.happiness

    def impact_on_happiness(self, terrain):
        self.happiness += terrain
        #Todo : rajouter des impact

    def set_zoom_size(self, a):
        self.zoom_size = a

    def get_zoom_size(self):
        return self.zoom_size

    def get_image(self):
        return self.image
