class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        print(self.height*2+self.width*2)

class Square:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        print(self.height*2+self.width*2)

rectangle = Rectangle(3,4)
rectangle.calculate_perimeter()
square = Square(4,5)
square.calculate_perimeter()
