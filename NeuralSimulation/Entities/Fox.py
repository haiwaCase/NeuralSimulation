from Entities.Entity import Entity
import pygame

class Fox(Entity, pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__(position, 20)
        self.image = pygame.image.load("Res/fox.png")
        self.rect = self.image.get_rect()
