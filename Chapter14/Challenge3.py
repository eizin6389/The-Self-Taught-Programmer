class Square:
    square_list = []

    def __init__(self, height, width):
        self.height = height
        self.width = width
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.height,self.width,self.height,self.width)

    def calculate_perimeter(self):
        print(self.height*2+self.width*2)

    def diff_object(self, obj1, obj2):
        return obj1 == obj2

square = Square(4,5)
square.calculate_perimeter()

for i in range(1,10):
    square.square_list.append(Square(i,i))

square.square_list.append(square)

for sq in square.square_list:
    sq.calculate_perimeter()
    print(sq)
    print(square.diff_object(square,sq))
