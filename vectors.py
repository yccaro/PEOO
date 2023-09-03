class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'vector({self.x}, {self.y})'

    def __add__(self, other):
        if (isinstance (other, vector)):
            x = self.x + other.x
            y = self.y + other.y
            return vector(x, y)

        else:
            x = self.x + other
            y = self.y + other
            return vector(x, y)

    def __sub__(self, other):
        if (isinstance (other, vector)):
            x = self.x - other.x
            y = self.y - other.y
            return vector(x, y)

        else:
            x = self.x - other
            y = self.y - other
            return vector(x, y)
    
    def __mul__(self, other):
        if (isinstance (other, vector)):
            x = self.x * other.x
            y = self.y * other.y
            return vector(x, y)

        else:
            x = self.x * other
            y = self.y * other
            return vector(x, y)

    def __truediv__(self, other):
        if (isinstance (other, vector)):
            x = self.x / other.x
            y = self.y / other.y
            return vector(x, y)

        else:
            x = self.x / other
            y = self.y / other
            return vector(x, y)

    def move(self, other):
        if (isinstance (other, vector)):
            self.x = self.x + other.x
            self.y = self.y + other.y

        else:
            self.x = self.x + other
            self.y = self.y + other
            
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
    
    def __neg__(self):
        return f'vector({self.x * -1}, {self.y * -1})'

    def __abs__(self):
        return (abs(self.y)-1) + (abs(self.x)-1)

    def rotage(self, angle):
        from math import sin, cos, radians

        angle = radians(angle)

        self.x = cos(angle) * self.x + sin(angle) * self.y
        self.y = - sin(angle) * self.x + cos(angle) * self.y
        
    def scale(self, other):
        if (isinstance (other, vector)):
            self.x = self.x * other.x
            self.y = self.y * other.y

        else:
            self.x = self.x * other
            self.y = self.y * other
    
    def copy(self):
        return vector(self.x, self.y)