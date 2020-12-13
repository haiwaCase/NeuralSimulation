import pygame

def change_image_scale(zoom, entity):
    entity.image = pygame.transform.scale(entity.image, (int(entity.image.get_width() / 2), int(entity.image.get_height() / 2)))
    print(zoom.get_zoom())
