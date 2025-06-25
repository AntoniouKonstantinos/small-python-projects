from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move) #Moves the ball when the game starts

    def bounce_wall(self):
        self.y_move *= -1 #Vertical axis direction

    def bounce_paddle(self):
        self.x_move *= -1 #Horizontal axis direction
        self.move_speed *= 0.9 #Increases speed of ball when hits a paddle

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle() #Changes the direction of the ball in horizontal axis
