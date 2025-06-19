from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

#Create the game screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake() #Create snake
food = Food()   #Create food
scoreboard = Scoreboard()

#Controling the snake using arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True
while playing:  #Game starts
    screen.update()
    time.sleep(0.3)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.update_score()
        food.refresh()
    #Detect collision with a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        playing = False
        scoreboard.game_over()
    #Detect collision with its tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            playing = False
            scoreboard.game_over()

screen.exitonclick()