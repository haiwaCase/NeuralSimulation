import pygame
from Entities.Entity import Entity

def load_image_fox(scale):
    image = pygame.image.load("Res/fox_256.png")
    return pygame.transform.rotozoom(image, 0, scale)

class Fox(Entity):

    def __init__(self, position):
        super().__init__(position, 20, "Res/fox_256.png")
        self.rect = self.image.get_rect()
