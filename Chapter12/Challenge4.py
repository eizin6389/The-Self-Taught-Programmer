import math

class Hexagon:
    def __init__(self, width):
        self.width = width

    def calculate_perimeter(self):
        print(self.width*6)

hexagon = Hexagon(3)
hexagon.calculate_perimeter()
