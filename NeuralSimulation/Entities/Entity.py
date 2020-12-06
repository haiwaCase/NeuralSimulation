class Entity:

    def __init__(self, position, happiness):
        self.position = position
        self.happiness = happiness

    def get_position(self):
        return self.position

    def get_happiness(self):
        return self.happiness

    def impact_on_happiness(self, terrain):
        self.happiness += terrain
        #to do : rajouter des impact

