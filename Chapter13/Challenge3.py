class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        print(self.height*2+self.width*2)

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rectangle = Rectangle(3,4)
rectangle.calculate_perimeter()
rectangle.what_am_i()
square = Square(4,5)
square.calculate_perimeter()
square.what_am_i()
