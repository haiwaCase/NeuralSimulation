import math

class Vec2:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def add_x(self, a):
        self.x += a

    def add_y(self, a):
        self.y += a

    def add_z(self, a):
        self.z += a

    def sub_x(self, a):
        self.x -= a

    def sub_y(self, a):
        self.y -= a

    def sub_z(self, a):
        self.z -= a

    def mul_x(self, a):
        self.x *= a

    def mul_y(self, a):
        self.y *= a

    def mul_z(self, a):
        self.z *= a

    def div_x(self, a):
        self.x /= a

    def div_y(self, a):
        self.y /= a

    def div_z(self, a):
        self.z /= a

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        self.z -= vec.z

    def mul(self, vec):
        self.x *= vec.x
        self.y *= vec.y
        self.z *= vec.z

    def div(self, vec):
        self.x /= vec.x
        self.y /= vec.y
        self.z /= vec.z

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def max(self):
        return max(self.x, self.y)

    def min(self):
        return min(self.x, self.y)

    def negate(self):
        self.x = -self.x
        self.y = -self.y

    def copy(self):
        return self

    def to_string(self):
        return str(self.x) + " " + str(self.y)

    def equals(self, vec):
        return self.x == vec.x and self.y == vec.y
