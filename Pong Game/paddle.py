from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.goto(start)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
