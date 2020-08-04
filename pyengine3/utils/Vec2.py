import math

__all__ = ["Vec2"]

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(self, xy = (0, 0)):
        return Vec2(xy[0], xy[1])
    
    def get_xy(self):
        return self.x, self.y
    
    def set_xy(self, x, y):
        self.x = x
        self.y = y
    
    def normalized(self):
        if len(self) == 0:
            return Vec2()
        else:
            Vec2(self.x / len(self), self.y / len(self))
    
    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        else:
            return Vec2(other - self.x, other - self.y)

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            return Vec2(int(self.x / other.x), int(self.y / other.y))
        else:
            return Vec2(int(self.x / other), int(self.y / other))

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return "Vec2" + str((self.x, self.y))

    def __eq__(self, other):
        return other is not None and isinstance(other, Vec2) and self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vec2(-self.x, -self.y)