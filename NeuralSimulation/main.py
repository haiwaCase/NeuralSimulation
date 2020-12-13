import pygame
import time
import json
import Render.Renderer as Renderer
from Entities.Fox import Fox
from Math.Vec2 import Vec2
from Utils.Zoom import Zoom

WIDTH = 1280
HEIGHT = 720

language = "fr_FR"

def load_title():
    with open(f"Lang/title_{language}.json") as json_data:
        data_dict = json.load(json_data)

    data_str = json.dumps(data_dict)

    loaded_json = json.loads(data_str)
    return loaded_json["Title"]

def update(entities, zoom):
    Renderer.update(pygame, entities, zoom)

def render(screen, entities, zoom):
    Renderer.render(pygame, screen, entities, zoom)

def main():
    load_title()
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(load_title())

    # Initialisation de l'objet zoom
    zoom = Zoom()

    # Intitialisation des entités
    vec = Vec2(0, 0, 0)
    fox = Fox(vec)

    vec_fox2 = Vec2(500, 0, 0)
    fox2 = Fox(vec_fox2)

    # Object list
    entities = [fox, fox2]

    while True:

        # Rendu à 60 images par seconde
        time.sleep(1 / 60)

        update(entities, zoom)
        render(screen, entities, zoom)

if __name__ == '__main__':
    main()
