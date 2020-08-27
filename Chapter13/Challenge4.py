class Rider:
    def __init__(self, name):
        self.name = name

class Hourse:
    def __init__(self, owner):
        self.owner = owner

    def show_name(self):
        print(self.owner.name)

rider = Rider("eizin")
hourse = Hourse(rider)
hourse.show_name()
