from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.head.shape("circle")

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def reset(self):
        for part in self.snake:
            part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.head.shape("circle")

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)