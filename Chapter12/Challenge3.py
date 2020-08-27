import math

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width*self.height/2)

triangle = Triangle(3,4)
triangle.area()
