class Fruit:
    def __init__(self, color='red', shape='round', count=0) -> None:
        self.color = color
        self.shape = shape
        self.count = count

    def eat(self):
        self.count = self.count - 1

class Apple(Fruit):

    def __init__(self, taste, color='red', shape='round', count=0) -> None:
        super().__init__(color, shape, count)
        self.taste = taste

    def eat(self, number):
        if self.count >= number:
            return self.count - number
