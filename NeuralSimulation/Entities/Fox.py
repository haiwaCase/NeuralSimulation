from Entities.Entity import Entity
import pygame

def load_image_fox(scale):
    image = pygame.image.load("Res/fox.png")
    return pygame.transform.rotozoom(image, 0, scale)

class Fox(Entity, pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__(position, 20)
        self.image = load_image_fox(scale=12)
        self.rect = self.image.get_rect()
