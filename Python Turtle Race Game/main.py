import turtle as t
import random

start_race = False
screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="PLACE YOUR BETS!", prompt="Pick the turtle to win the race. Pick a color")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtles = []
y = -125
winner = ""

for index in range(6):
    john = t.Turtle("turtle")
    john.color(colors[index])
    john.penup()
    john.goto(-240, y)
    y += 50
    turtles.append(john)

if bet:
    start_race = True

while start_race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            start_race = False
            winner = turtle.fillcolor()
            if winner == bet.lower():
                print(f"You Win. {winner} turtle won the race")
            else:
                print(f"You Lose. {winner} turtle won the race")
            break

screen.exitonclick()



