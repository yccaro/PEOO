class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return vector(x, y)

    def move(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y :
            return True
        else:
            return False

    def __ne__(self, other):
        if not(self.x == other.x and self.y == other.y) :
            return True
        else:
            return False

    def __abs__(self):
        
v = vector(0, 1)
v1 = vector(0, 1)
print(v != v1)