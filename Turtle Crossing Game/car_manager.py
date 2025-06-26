from turtle import Turtle
from random import randint, choice

COLORS = ["yellow", "orange", "red", "green", "aqua", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.traffic = []
        self.speed = STARTING_MOVE_DISTANCE

    """Creates a car in traffic randomly about 1 in 6 times the games loops"""
    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            self.traffic.append(new_car)

    """Moves every car on traffic"""
    def move_cars(self):
        for car in self.traffic:
            car.forward(self.speed)

    """The cars speed up for the next level when we pass current level"""
    def level_up(self):
        self.speed += MOVE_INCREMENT
