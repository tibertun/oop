import turtle

class Figure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.fill = "white"

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setFillColor(self, c):
        self.fill = c

    def show(self):
        self.draw(self.fill)

    def draw(self, color):
        pass

class Klitunka(Figure):
    def draw(self, color):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()

class Shashka(Figure):
    def draw(self, color):
        turtle.penup()
        turtle.goto(self.x + 25, self.y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()

def draw_shashki():
    for i in range(3):
        for j in range(8):
            if (i + j) % 2 == 1:
                s = Shashka()
                s.setPosition(j*50-200, i*50-200)
                s.setFillColor("black")
                s.show()

    for i in range(5,8):
        for j in range(8):
            if (i + j) % 2 == 1:
                s = Shashka()
                s.setPosition(j*50 - 200, i*50 - 200)
                s.setFillColor("white")
                s.show()

def draw_board():
    for i in range(8):
        for j in range(8):
            k = Klitunka()
            k.setPosition(j*50-200, i*50-154)
            if (i + j) % 2 == 0:
                k.setFillColor("white")
            else:
                k.setFillColor("gray")
            k.show()

turtle.speed(100)
turtle.hideturtle()
draw_board()
draw_shashki()
turtle.done()