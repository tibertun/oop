from random import randint
import math

def plosha_trikutnik(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    if s <= 0:
        return 0
    return s ** 0.5
def perimeter_trikutnik(a, b, c):
    return a + b + c
def is_normalni_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a

MAX = 25 #масімальний розмір
MULT = 4 #масштаб
# фігури = кількість параметрів
Figures = {"Triangle" : 3,                     # Трикутник
           "Rectangle" : 2,                    # Прямокутник
           "Trapeze" : 4,                      # Трапеція
           "Parallelogram" : 3,                # Паралелограм
           "Circle" : 1,                       # Круг
           "Ball" : 1,                         # Куля
           "TriangularPyramid" : 2,            # Трикутна піраміда
           "QuadrangularPyramid" : 3,          # Чотирикутна піраміда
           "RectangularParallelepiped" : 3,    # Прямокутний паралелепіпед
           "Cone" : 2,                         # Конус
           "TriangularPrism" : 4}              # Трикутна Призма

FigureNames = list(Figures.keys())

def generate(fname, figures_number):
    FIGURE_COUNT = len(FigureNames)

    with open(fname, "w", encoding='utf-8') as f_out:
        for i in range(figures_number):

            figure = FigureNames[randint(0, FIGURE_COUNT - 1)]
            print("%30s" % figure, file=f_out, end=" ")

            val_num = Figures[figure]
            for i in range(val_num):
                val = randint(0, MAX)
                print("%4d" % val, file=f_out, end=" ")

            print(file=f_out)

class Figure:
    def rozmirnist(self):
        return None

    def obchislenya(self):
        return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def rozmirnist(self):
        return 2

    def obchislenya(self):
        return plosha_trikutnik(self.a, self.b, self.c)


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def rozmirnist(self):
        return 2

    def obchislenya(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def rozmirnist(self):
        return 2

    def obchislenya(self):
        return math.pi * self.r ** 2

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        return 4 / 3 * math.pi * self.r ** 3

class Cone(Figure):
    def __init__(self, r, h):
        self.r, self.h = r, h

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        return (1 / 3) * math.pi * self.r ** 2 * self.h

class RectangularParallelepiped(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        return self.a * self.b * self.c


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        return super().obchislenya() * self.h


class TriangularPyramid(Figure):
    def __init__(self, a, h):
        self.a, self.h = a, h

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        s = (3 ** 0.5 / 4) * self.a ** 2
        return s * self.h / 3


class QuadrangularPyramid(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def rozmirnist(self):
        return 3

    def obchislenya(self):
        return self.a * self.b * self.h / 3


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def rozmirnist(self):
        return 2

    def obchislenya(self):
        return (self.a + self.b)/2 * self.c


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def rozmirnist(self):
        return 2

    def obchislenya(self):
        return self.a * self.h


def create_figure(parts):
    name = parts[0]
    nums = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*nums)
    if name == "Rectangle":
        return Rectangle(*nums)
    if name == "Trapeze":
        return Trapeze(*nums)
    if name == "Parallelogram":
        return Parallelogram(*nums)
    if name == "Circle":
        return Circle(*nums)
    if name == "Ball":
        return Ball(*nums)
    if name == "TriangularPyramid":
        return TriangularPyramid(*nums)
    if name == "QuadrangularPyramid":
        return QuadrangularPyramid(*nums)
    if name == "RectangularParallelepiped":
        return RectangularParallelepiped(*nums)
    if name == "Cone":
        return Cone(*nums)
    if name == "TriangularPrism":
        return TriangularPrism(*nums)


def find_max(filename):
    max_s = 0
    max_name = ""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            fig = create_figure(parts)
            s = fig.obchislenya()

            if s > max_s:
                max_s = s
                max_name = parts[0]

    print(filename, max_name, max_s)


if __name__ == "__main__":
    generate("input3.3.1.txt", 100)
    generate("input3.3.2.txt", 500)
    generate("input3.3.3.txt", 1000)

    find_max("input3.3.1.txt")
    find_max("input3.3.2.txt")
    find_max("input3.3.3.txt")
