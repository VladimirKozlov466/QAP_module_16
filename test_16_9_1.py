
import math


class Figures:
    def __init__(self, name=None):
        self.name = name


class Square(Figures):
    def __init__(self, name, a):
        super().__init__(name)
        self.a = a

    def getArea_square(self):
        return self.a ** 2

    def get_square_info(self):
        return '{0} ({1})'.format(self.name, self.a)


class Circle(Figures):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def getArea_cicle(self):
        return math.pi * self.r ** 2

    def get_circle_info(self):
        return '{0} ({1})'.format(self.name, self.r)


class Rectangle(Figures):
    def __init__(self,name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def getArea_rectangle(self):
        return self.a * self.b

    def get_rectangle_info(self):
        return '{0} ({1}, {2})'.format(self.name, self.a, self.b)


class Triangle(Figures):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def getArea_triangle(self):
        p = (self.a + self.b + self.c)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def get_triangle_info(self):
        return '{0} ({1}, {2}, {3})'.format(self.name, self.a, self.b, self.c)


Square = Square("Square", 5)
print(Square.get_square_info())

Circle = Circle("Circle", 5)
print(Circle.get_circle_info())

Rectangle = Rectangle("Rectangle", 5, 10)
print(Rectangle.get_rectangle_info())

Triangle = Triangle("Triangle", 5, 6, 7)
print(Triangle.get_triangle_info())

