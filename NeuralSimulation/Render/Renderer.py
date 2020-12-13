import sys
import Utils.Resizer as Resizer
from Entities.Fox import Fox

def update(pygame, entities, zoom):
    # Gestion des inputs
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom.set_zoom(zoom.get_zoom() + 10)
                print(zoom.to_string())
            if event.button == 5:
                zoom.set_zoom(zoom.get_zoom() - 10)
                print(zoom.to_string())
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Interaction avec la physique des entitées
    for entity in entities:
        entity.set_position_x(entity.get_position().get_x() + 2)
        entity.set_position_y(entity.get_position().get_y() + 2)
        entity.set_zoom_size(zoom)

def render(pygame, screen, entities, zoom):
    # Clear l'écran à chaque itération
    screen.fill((0, 0, 0))
    for entity in entities:
        screen.blit(entity.image, (entity.get_position().get_x(), entity.get_position().get_y()))
        if type(entity) is Fox:
            print("mpm")
            Resizer.change_image_scale(zoom, entity)

    pygame.display.flip()
