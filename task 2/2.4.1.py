import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)

class Digit:
    def __init__(self, value, radius):
        self.value = value
        self.radius = radius

    def draw(self, t):
        angle = math.radians(90 - self.value * 30)
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        t.penup()
        t.goto(x, y -8)
        t.color("black")
        t.write(self.value, align="center", font=("Arial", 14, "bold"))

class ClockFace:
    def __init__(self, radius):
        self.radius = radius
        for i in range(1, 13):
            self.digits.append(Digit(i, radius - 25))

    def draw(self, t):
        t.penup()
        t.goto(0, -self.radius)
        t.pendown()
        t.color("black", "white")
        t.width(2)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()
        for d in self.digits:
            d.draw(t)

class Hand:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def draw(self, t, angle):
        t.penup()
        t.goto(0, 0)
        t.setheading(90 - angle)
        t.color(self.color)
        t.width(self.width)
        t.pendown()
        t.forward(self.length)


t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(0)

t2 = turtle.Turtle()
t2.hideturtle()
t2.speed(0)

face = ClockFace(160)
h1 = Hand(70, 6, "blue")
h2 = Hand(110, 3, "lightgray")
h3 = Hand(130, 1, "red")

face.draw(t1)

def update():
    t2.clear()
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    h1.draw(t2, (hour + minute / 60) * 30)
    h2.draw(t2,(minute + second / 60) * 6)
    h3.draw(second * 6)

    t2.penup()
    t2.goto(0, 0)
    t2.dot(10, "white")

    screen.update()
    screen.ontimer(update, 1000)

update()
turtle.done()
