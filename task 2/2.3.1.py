import turtle

t = turtle.Turtle()
t.speed(0)
class Petal:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        for _ in range(2):
            t.circle(self.size, 60)
            t.left(120)
        t.end_fill()

class Leaf:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        t.left(45)
        t.circle(self.size, 90)
        t.left(90)
        t.circle(self.size, 90)
        t.end_fill()

class Stem:
    def __init__(self, length):
        self.length = length
    def draw(self,t):
        t.color('green')
        t.width(3)
        t.right(90)
        t.forward(self.length)
        t.left(90)

class Flower:
    def __init__(self, x, y, petal_color):
        self.x = x
        self.y = y
        self.petal = Petal(petal_color, 50)
        self.leaf = Leaf("green", 30)
        self.stem = Stem(150)

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(0)
        t.pendown()

        for _ in range(6):
            self.petal.draw(t)
            t.left(60)
        t.color("yellow")
        t.begin_fill()
        t.goto(self.x, self.y - 10)
        t.circle(10)
        t.end_fill()

        t.penup()
        t.goto(self.x, self.y - 50)
        t.pendown()
        self.stem.draw(t)

        t.penup()
        t.goto(self.x, self.y - 110)
        t.pendown()
        t.left(45)
        self.leaf.draw(t)
        t.right(45)

flowers = [
    Flower(-150, 100, "red"),
    Flower(0, 100, "blue"),
    Flower(150, 100, "purple")
]

for f in flowers:
    f.draw(t)

turtle.done()