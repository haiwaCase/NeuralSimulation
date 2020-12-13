class Zoom:

    def __init__(self):
        self.zoom = 1

    def get_zoom(self):
        return self.zoom

    def set_zoom(self, z):
        if self.zoom <= 1:
            self.zoom = 1
        self.zoom = z

    def to_string(self):
        return str(self.zoom)
