import pygame
import time
import Render.Renderer as Renderer

def update():
    Renderer.update(pygame)

def render():
    Renderer.render(pygame)

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("NeuralSimulation")

    running = True

    while running:

        # Rendu à 60 images par seconde
        time.sleep(1 / 60)

        update()
        render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

if __name__ == '__main__':
    main()
