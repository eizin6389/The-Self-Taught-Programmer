import math

class Circle:
    def __init__(self, width):
        self.width = width

    def area(self):
        print(self.width*self.width*math.pi)

circle = Circle(3)
circle.area()
