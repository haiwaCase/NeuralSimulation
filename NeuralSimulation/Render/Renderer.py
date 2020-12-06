def update(pygame, entities):
    for entity in entities:
        entity.set_position_x(entity.get_position().get_x() + 2)
        entity.set_position_y(entity.get_position().get_y() + 2)

def render(pygame, screen, entities):
    screen.fill((0, 0, 0))
    for entity in entities:
        screen.blit(entity.image, (entity.get_position().get_x(), entity.get_position().get_y()))
    pygame.display.flip()
