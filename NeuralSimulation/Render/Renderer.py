import sys
import pygame
from Entities.Fox import Fox

def update(entities, zoom):
    # Gestion des inputs

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                #zoom.set_zoom(zoom.get_zoom() + 10)
                print(zoom.to_string())
            if event.button == 5:
               #zoom.set_zoom(zoom.get_zoom() - 10)
                print(zoom.to_string())
            if event.button == 3:
                print("Right clicking")
                pygame.mouse.set_visible(False)
                pygame.mouse.set_pos((pygame.display.get_surface().get_width() / 2, pygame.display.get_surface().get_height() / 2))
                pygame.event.set_grab(True)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                print("Not right clicking")
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Interaction avec la physique des entitées
    for entity in entities:
        #entity.set_position_x(entity.get_position().get_x() + 2)
        #entity.set_position_y(entity.get_position().get_y() + 2)
        entity.set_zoom_size(zoom)

def render(screen, entities, zoom):
    # Clear l'écran à chaque itération
    screen.fill((0, 0, 0))
    for entity in entities:
        screen.blit(entity.image, (entity.get_position().get_x(), entity.get_position().get_y()))

    pygame.display.flip()
