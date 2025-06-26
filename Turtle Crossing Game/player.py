from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.move_to_start()
        self.setheading(90)

    """Move the turtle on the 'Up' key stroke"""
    def move(self):
        self.forward(MOVE_DISTANCE)

    """Resets the turtle after has reached the top"""
    def move_to_start(self):
        self.goto(STARTING_POSITION)