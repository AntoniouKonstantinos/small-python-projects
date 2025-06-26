from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

john = Player()
level = Scoreboard()
traffic = CarManager()

screen.listen()
screen.onkey(john.move,"Up")

playing = True
while playing:
    time.sleep(0.1)
    screen.update()
    traffic.create_car()
    traffic.move_cars()
    #Detect when turtle has reached the top
    if john.ycor() > 280:
        john.move_to_start()
        level.update_score()
        traffic.level_up()
    #Detect collision with a car
    for car in traffic.traffic:
        if john.distance(car) < 20:
            level.game_over()
            playing = False

screen.exitonclick()