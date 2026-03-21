import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimeter(self):
        return self.a + self.b + self.c
    def plosha(self):
        p = self.perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def show(self):
        return "Triangle({}, {}, {})".format(self.a, self.b, self.c)

class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def plosha(self):
        return self.a * self.b
    def show(self):
        return "Rectangle({}, {})".format(self.a, self.b)

class Circle:
    def __init__(self, r):
        self.r = float(r)
    def perimeter(self): # довжина кола
        return 2 * math.pi * self.r
    def plosha(self):
        return math.pi * self.r ** 2
    def show(self):
        return "Circle({})".format(self.r)

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)
        self.b = float(b)
        self.h = float(h)
    def perimeter(self):
        return 2 * (self.a + self.b)
    def plosha(self):
        return self.a * self.h
    def show(self):
        return "Parallelogram({}, {}, {})".format(self.a, self.b, self.h)

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def plosha(self):
        try:
            val = self.c ** 2 - ((self.c ** 2 - self.d ** 2 + (self.b - self.a) ** 2) / (2 * (self.b - self.a))) ** 2
            if val < 0:
                raise ValueError("- under sprt")
            return (self.a + self.b) * math.sqrt(val) / 2
        except (ValueError, ZeroDivisionError):
            return -1
    def show(self):
        return "Trapeze({},{},{},{})".format(self.a,self.b,self.c,self.d)

def read_figures(filename):
    figures = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.split()
                name = parts[0]
                if name == "Triangle":
                    figures.append(Triangle(float(parts[1]), float(parts[2]), float(parts[3])))
                elif name == "Rectangle":
                    figures.append(Rectangle(float(parts[1]), float(parts[2])))
                elif name == "Circle":
                    figures.append(Circle(float(parts[1])))
                elif name == "Parallelogram":
                    figures.append(Parallelogram(float(parts[1]), float(parts[2]), float(parts[3])))
                elif name == "Trapeze":
                    figures.append(Trapeze(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))

    except FileNotFoundError:
        print("File not found")
    return figures

def find_max(figures):
    figures = [f for f in figures if f.plosha() >= 0]
    if not figures:
        print("No figures")
        return
    max_plosha = max(figures, key = lambda x: x.plosha())
    max_perimeter = max(figures, key = lambda x: x.perimeter())
    print("largest area:")
    print(max_plosha.show())
    print("plosha =", max_plosha.plosha())

    print("largest perimeter:")
    print(max_perimeter.show())
    print("perimeter =", max_perimeter.perimeter())

figures = read_figures("input01.txt")
find_max(figures)
figures = read_figures("input02.txt")
find_max(figures)
figures = read_figures("input03.txt")
find_max(figures)
