from random import randint
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed(18)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))