class Entity:

    def __init__(self, position, happiness):
        self.position = position
        self.happiness = happiness

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def set_position_x(self, x):
        self.position.set_x(x)

    def set_position_y(self, y):
        self.position.set_y(y)

    def get_happiness(self):
        return self.happiness

    def impact_on_happiness(self, terrain):
        self.happiness += terrain
        #Todo : rajouter des impact

