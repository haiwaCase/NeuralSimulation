import pygame
from Entities.Entity import Entity

def load_image_fox(scale):
    image = pygame.image.load("Res/fox_256.png")
    return pygame.transform.rotozoom(image, 0, scale)

class Fox(Entity, pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__(position, 20)
        self.image = load_image_fox(scale=self.zoom_size)
        self.rect = self.image.get_rect()

    def set_image_scale(self, scale):
        pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        print(self.image.get_width())
        print(self.image.get_height())
