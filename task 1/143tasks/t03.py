import turtle
import math
import time
from random import randint
rand = randint(0,10)

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0) # абсолютна позиція першої вершини
        self.vertex1 = (x1, y1) # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2) # позиція третьої відносно першої вершини
        self.color = "black" # колір трикутника за промовчанням

    def set_rotation(self, rotation):
        self.rotation = rotation
    def set_scale(self, scale):
        self.scale = scale
    def set_position(self, x, y):
        self.position = (x, y)
    def get_absolute_vertices(self):
        x0, y0 =self.position
        x1, y1 = x0+ self.vertex1[0], y0 + self.vertex1[1]
        x2, y2 = x0+ self.vertex2[0], y0 + self.vertex2[1]
        return (x0, y0), (x1, y1), (x2, y2)
    def set_color(self, color):
        self.color = color
        t.color(self.color)

    def _transform(self, x, y):
        px, py = self.position
        tx = x- px
        ty = y- py
        tx *= self.scale[0]
        ty *= self.scale[1]

        rx = tx * math.cos(self.rotation)- ty * math.sin(self.rotation)
        ry = ty * math.cos(self.rotation) + ty * math.sin(self.rotation)
        return px+rx, py+ry

    def draw(self):
        t.color(self.color)
    def draw(self,t):
        x0,y0 = self.position
        dx1, dy1 = self.vertex1
        dx2, dy2 = self.vertex2

        point1 = (x0+ dx1, y0+ dy1)
        point2 = (x0+ dx2, y0+ dy2)

        t.penup()
        t.goto(x0,y0)
        t.pendown()

        t.fillcolor(self.color)
        t.begin_fill()

        t.goto(point1)
        t.goto(point2)
        t.goto(x0, y0)
        t.end_fill()

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(10)
t.width(2)
t.hideturtle()

colors = ["red","blue","green","yellow","purple","orange"]


for _ in range(100):

    while True:
        rand_x1 = randint(-60,60)
        rand_y1 = randint(-60, 60)
        rand_x2 = randint(-60, 60)
        rand_y2 = randint(-60, 60)
        if (rand_x1 * rand_y2)-(rand_x2-rand_y1)!=0:
            break

    my_triangle = Triangle(rand_x1, rand_y1, rand_x2, rand_y2)

    pos_x = randint(-350,350)
    pos_y = randint(-300,300)
    my_triangle.set_position(pos_x, pos_y)

    my_triangle.set_color(colors[randint(0,5)])
    my_triangle.draw(t)

turtle.done()
time.sleep(1)
t.clear()

anim_tri = Triangle(120,0,60,160)
anim_tri.set_position(0, 0)
anim_tri.set_color("black")

for angle in range(0,360):
    t.clear()
    anim_tri.set_rotation(math.radians(angle))
    anim_tri.draw(t)
    turtle.update()
anim_tri.set_rotation(0)
turtle.done()