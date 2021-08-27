class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def getArea_rectangle(self):
        return self.length * self.width

    def get_rectangle_info(self):
        return 'Rectangle length = {0}, Rectangle width = {1}'.format(self.length, self.width)

rectangle_1 = Rectangle(100, 50)
print(rectangle_1.get_rectangle_info())

