from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

START_L = (-370, 0)
START_R = (370, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

paddle_l = Paddle(START_L) #Create the left paddle
paddle_r = Paddle(START_R) #Create the right paddle
ball = Ball() #Create the ball
scoreboard = Scoreboard() # Create the scoreboard

screen.listen()
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

playing = True
while playing:  #Game starts
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with upper and lower boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    #Detect collision with a paddle
    if (ball.xcor() > 340 and ball.distance(paddle_r) < 50) or (ball.xcor() < -340 and ball.distance(paddle_l) < 50):
        ball.bounce_paddle()
    # Detect when the ball misses right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.update_score(1) # flag equals 1, left paddle wins
    # Detect when the ball misses left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.update_score(0) # flag equals 0, right paddle wins



screen.exitonclick()