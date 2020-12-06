import pygame
import time
import json
import Render.Renderer as Renderer

WIDTH = 1280
HEIGHT = 720

language = "fr_FR"

def load_title():
    with open(f"Lang/title_{language}.json") as json_data:
        data_dict = json.load(json_data)

    data_str = json.dumps(data_dict)

    loaded_json = json.loads(data_str)
    return loaded_json["Title"]

def update():
    Renderer.update(pygame)

def render():
    Renderer.render(pygame)

def main():
    load_title()
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neural Simulation")

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
