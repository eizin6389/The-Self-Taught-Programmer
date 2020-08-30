class Square:
    square_list = []

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        print(self.height*2+self.width*2)

square = Square(4,5)
square.calculate_perimeter()

for i in range(1,10):
    square.square_list.append(Square(i,i))

for sq in square.square_list:
    sq.calculate_perimeter()
