from turtle import Turtle

FONT = ("Courier", 8 ,"normal")

class StatesNames(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_name(self, x, y, name):
        self.goto(x, y)
        self.write(name, False, "center", FONT)