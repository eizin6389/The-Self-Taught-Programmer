class Apple:
    def __init__(self, color, weight, height, width):
        self.color = color
        self.weight = weight
        self.height = height
        self.width = width
        print("Create")

    def change(self):
        print("Change")

apple = Apple("red",2,6,8)
apple.change()
